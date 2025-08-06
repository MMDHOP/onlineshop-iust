from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , request , response 
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.db.models import Q

from rest_framework import generics , permissions, status 
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import settings

from functools import reduce
from operator import or_

from .serializers import StepSerializer , RoutineSerializer

from quiz.models import Quiz
from products.models import Product
from .models import Routine



# Create your views here.



def generate_routine_from_quiz(user, quiz_data, plan_name="Full Plan"):
    steps = []

    skin_type = quiz_data['skin_type']
    concerns = quiz_data['concerns']
    preferences = quiz_data.get('preferences', [])

    skin_type_filter = reduce(or_, [Q(skin_type__icontains=stype) for stype in skin_type]) if skin_type else Q()
    concern_filter = reduce(or_, [Q(concern_targeted__icontains=c) for c in concerns]) if concerns else Q()
    preference_filter = reduce(or_, [Q(preferences__icontains=p) for p in preferences]) if preferences else Q()

    def get_best_product(category, filter_skin=True):
        base_query = Product.objects.filter(category=category)

        if filter_skin:
            base_query = base_query.filter(skin_type_filter)
        return base_query.filter(concern_filter, preference_filter).order_by('-rating').first()

    # محصولات پیشنهادی برای هر مرحله از روتین
    product_steps = [
        ("Cleanser", True),
        ("Toner-Essence", True),
        ("Serum-Treatments", False),   # بدون فیلتر skin_type
        ("Moisturizer", True),
        ("Sunscreen", True),
        ("Exfoliator", False),         # بدون فیلتر skin_type
        ("Eye-Care", True),
        ("Mask", True),
    ]

    for step_name, filter_skin in product_steps:
        product = get_best_product(step_name, filter_skin)
        if product:
            steps.append({"step_name": step_name, "product_id": product.id})
        else:
            steps.append({"step_name": step_name, "product_id": None})  # اگر محصولی پیدا نشد

    # ایجاد روتین
    routine = Routine.objects.create(
        user=user,
        plan_name=plan_name,
        steps=steps
    )
    return routine



class GenerateRoutineFromQuiz(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        quiz = Quiz.objects.filter(user=request.user).order_by('-timestamp').first()
        if not quiz:
            return Response({"error": "No quiz data found"}, status=400)

        quiz_data = {
            "skin_type": quiz.skin_type,
            "concerns": quiz.concern_targeted,
            "preferences": quiz.preferences
        }

        routine = generate_routine_from_quiz(request.user, quiz_data)
        return Response({
            "message": "Routine created successfully",
            "routine_id": routine.routine_id,
            "steps": routine.steps
        })







class UserRoutineView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        routine = Routine.objects.filter(user=request.user).order_by('-created_at').first()
        if routine:
            return Response(RoutineSerializer(routine).data)
        return Response({"detail": "No routine found."}, status=404)





def user_routine_page(request):
    routine = Routine.objects.filter(user=request.user).order_by('-created_at').first()
    detailed_steps = []

    if routine:
        for step in routine.steps:
            product_id = step.get('product_id')
            product = Product.objects.filter(id=product_id).first()
            detailed_steps.append({
                'step_name': step.get('step_name'),
                'product': product  # ممکنه None باشه
            })

    context = {
        'routine': routine,
        'detailed_steps': detailed_steps,
    }
    return render(request, 'routine.html', context)
