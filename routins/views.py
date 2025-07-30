from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , request , response 
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from rest_framework import generics , permissions, status 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import settings

from .serializers import StepSerializer , RoutineSerializer

from quiz.models import Quiz
from products.models import Product
from .models import Routine



# Create your views here.

def generate_routine_from_quiz(user, quiz_data, plan_name="Full Plan"):
    # فرض بر اینکه quiz_data شامل skin_type، concerns و غیره است.
    steps = []

    cleanser = Product.objects.filter(
        category="cleanser",
        skin_type__contains=quiz_data['skin_type'],
        concern_targeted__overlap=quiz_data['concerns']
    ).order_by('-rating').first()
    if cleanser:
        steps.append({"step_name": "Cleanser", "product_id": cleanser.id})

    toner = Product.objects.filter(
        category="Toner-Essence",
        skin_type__contains=quiz_data['skin_type'],
        concern_targeted__overlap=quiz_data['concerns']
    ).order_by('-rating').first()
    if toner:
        steps.append({"step_name": "Toner-Essence", "product_id": toner.id})


    serum = Product.objects.filter(
        category="Serum-Treatments",
        concern_targeted__overlap=quiz_data['concerns']
    ).order_by('-rating').first()
    if serum:
        steps.append({"step_name": "Serum-Treatments", "product_id": serum.id})


    Moisturizer = Product.objects.filter(
        category="Moisturizer",
        skin_type__contains=quiz_data['skin_type'],
        concern_targeted__overlap=quiz_data['concerns']
    ).order_by('-rating').first()
    if Moisturizer:
        steps.append({"step_name": "Moisturizer", "product_id": Moisturizer.id})

    Sunscreen = Product.objects.filter(
        category="Sunscreen",
        skin_type__contains=quiz_data['skin_type'],
        concern_targeted__overlap=quiz_data['concerns']
    ).order_by('-rating').first()
    if Sunscreen:
        steps.append({"step_name": "Sunscreen", "product_id": Sunscreen.id})


    Exfoliator = Product.objects.filter(
        category="Exfoliator",
        concern_targeted__overlap=quiz_data['concerns']
    ).order_by('-rating').first()
    if Exfoliator:
        steps.append({"step_name": "Exfoliator", "product_id": Exfoliator.id})


    Eye_Care = Product.objects.filter(
        category="Eye-Care",
        skin_type__contains=quiz_data['skin_type'],
        concern_targeted__overlap=quiz_data['concerns']
    ).order_by('-rating').first()
    if Eye_Care:
        steps.append({"step_name": "Eye-Care", "product_id": Eye_Care.id})

    Mask = Product.objects.filter(
        category="Mask",
        skin_type__contains=quiz_data['skin_type'],
        concern_targeted__overlap=quiz_data['concerns']
    ).order_by('-rating').first()
    if Mask:
        steps.append({"step_name": "Mask", "product_id": Mask.id})


    routine = Routine.objects.create(
        user=user,
        plan_name=plan_name,
        steps=steps
    )
    return routine




class GenerateRoutineFromQuiz(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        quiz = Quiz.objects.filter(user=request.user).order_by('-created_at').first()
        if not quiz:
            return Response({"error": "No quiz data found"}, status=400)

        quiz_data = {
            "skin_type": quiz.skin_type,
            "concerns": quiz.concerns,
            "preferences": quiz.preferences
        }

        routine = generate_routine_from_quiz(request.user, quiz_data)
        return Response({
            "message": "Routine created successfully",
            "routine_id": routine.routine_id,
            "steps": routine.steps
        })





from rest_framework.generics import RetrieveAPIView


class UserRoutineView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        routine = Routine.objects.filter(user=request.user).order_by('-created_at').first()
        if routine:
            return Response(RoutineSerializer(routine).data)
        return Response({"detail": "No routine found."}, status=404)




def user_routine_page(request):
    # گرفتن آخرین روتین ساخته شده برای کاربر
    routine = Routine.objects.filter(user=request.user).order_by('-created_at').first()

    context = {
        'routine': routine,
    }

    return render(request, 'routine.html', context)