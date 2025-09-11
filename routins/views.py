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
from datetime import datetime  

from .serializers import StepSerializer , RoutineSerializer

from quiz.models import Quiz
from products.models import Product
from .models import Routine


def get_current_season():

    current_month = datetime.now().month
    
    if current_month in [12, 11, 10]:
        return 'winter' 
    elif current_month in [1, 2, 3]:
        return 'spring'  
    elif current_month in [4, 5, 6]:
        return 'autumn'  
    elif current_month in [7, 8, 9]:
        return 'summer'  

def get_seasonal_message():

    current_season = get_current_season()
    
    seasonal_messages = {
        'spring': {
            'title': 'Spring Skincare Tips',
            'icon': '🌸',
            'message': 'Spring brings renewal and fresh energy to your skincare routine. Your skin needs gentle cleansers and lightweight moisturizers. Seasonal allergies may make your skin more sensitive, so incorporate anti-inflammatory products.',
            'tips': [
                'Use SPF 30+ sunscreen daily',
                'Choose gentle, non-irritating cleansers', 
                'Switch to lightweight moisturizers',
                'Add anti-allergy products to your routine'
            ]
        },
        'summer': {
            'title': 'Summer Skincare Protection',
            'icon': '☀️',
            'message': 'Summer demands maximum sun protection and oil control. Your skin produces more sebum in hot weather, requiring stronger cleansers and waterproof sunscreens to maintain healthy skin.',
            'tips': [
                'Apply SPF 50+ sunscreen every 2 hours',
                'Use oil-controlling cleansers',
                'Choose water-based, lightweight moisturizers',
                'Keep hydrating mists for midday refresh'
            ]
        },
        'autumn': {
            'title': 'Autumn Skin Preparation',
            'icon': '🍂',
            'message': 'Autumn is the perfect time to prepare your skin for winter. The air becomes drier, and your skin needs strengthening treatments and richer formulations to maintain its barrier function.',
            'tips': [
                'Transition to richer moisturizers',
                'Add Vitamin C serums for protection',
                'Incorporate gentle exfoliation weekly',
                'Begin using nourishing facial oils'
            ]
        },
        'winter': {
            'title': 'Winter Intensive Care',
            'icon': '❄️',
            'message': 'Winter is the most challenging season for your skin. Cold, dry air strips moisture from your skin, causing tightness and flaking. Focus on intensive hydration and barrier repair.',
            'tips': [
                'Use heavy, occlusive moisturizers',
                'Avoid hot water when cleansing',
                'Add hyaluronic acid serums',
                'Use a humidifier in your bedroom'
            ]
        }
    }
    
    return seasonal_messages.get(current_season, seasonal_messages['spring'])


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

    product_steps = [
        ("Cleanser", True),           
        ("Toner-Essence", True),      
        ("Serum-Treatments", False),  
        ("Moisturizer", True),        
        ("Sunscreen", True),          
        ("Exfoliator", False),        
        ("Eye-Care", True),           
        ("Mask", True),               
    ]

    for step_name, filter_skin in product_steps:
        product = get_best_product(step_name, filter_skin)
        if product:
            steps.append({"step_name": step_name, "product_id": product.id})
        else:
            steps.append({"step_name": step_name, "product_id": None})  

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
                'product': product  
            })

    seasonal_info = get_seasonal_message()
    current_season = get_current_season()

    context = {
        'routine': routine,
        'detailed_steps': detailed_steps,
        'seasonal_info': seasonal_info,  
        'current_season': current_season,  
    }
    
    return render(request, 'routine.html', context)