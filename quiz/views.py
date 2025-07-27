from django.shortcuts import render

# Create your views here.
# quiz/views.py


QUESTIONS = [
    "How oily is your skin typically?",
    "How often do you experience acne or breakouts?",
    "How sensitive is your skin to skincare products?",
    "How dry does your skin feel after washing it?",
    "How often do you exfoliate your skin?",
    "How much sun exposure do you get daily?",
    "How hydrated does your skin feel?",
    "Do you have dark spots or pigmentation issues?",
    "How tight does your skin feel during the day?",
    "How often do you use skincare products (e.g. serums, moisturizers)?"
]

OPTIONS = ["Very Low", "Low", "Medium", "High", "Very High"]

SCORE_MAP = {
    "Very Low": 1,
    "Low": 2,
    "Medium": 3,
    "High": 4,
    "Very High": 5,
}

RECOMMENDATIONS = {
    0: {
        1: "Your skin seems very dry. Use rich moisturizers.",
        2: "Slightly dry skin. Use hydrating toner.",
        3: "Balanced skin. Maintain current care.",
        4: "Oily tendency. Use oil-free products.",
        5: "Very oily skin. Use mattifying products.",
    },
    1: {
        1: "Rare breakouts. Keep a simple routine.",
        2: "Occasional pimples. Cleanse gently.",
        3: "Moderate acne. Consider salicylic acid.",
        4: "Frequent acne. Use targeted treatments.",
        5: "Severe acne. See a dermatologist.",
    },
    2: {
        1: "Skin not sensitive. You have flexibility.",
        2: "Low sensitivity. Still avoid fragrance.",
        3: "Medium sensitivity. Patch test new products.",
        4: "High sensitivity. Stick to hypoallergenic items.",
        5: "Very sensitive. Consult with specialist.",
    },
    3: {
        1: "Very dry after washing. Use oil-based cleanser.",
        2: "Mild tightness. Try cream cleanser.",
        3: "Neutral. Any mild cleanser should work.",
        4: "Slight oil after wash. Use gel-based.",
        5: "Very oily post-wash. Consider foaming cleanser.",
    },
    4: {
        1: "Never exfoliate. Start with once a week.",
        2: "Rare exfoliation. Increase gradually.",
        3: "Moderate. Keep your routine.",
        4: "Frequent exfoliation. Watch for irritation.",
        5: "Too frequent. You may be overdoing it.",
    },
    5: {
        1: "Avoid sun as much as possible.",
        2: "Use SPF daily.",
        3: "SPF is essential during daytime.",
        4: "Consider hats/sunglasses.",
        5: "You need strong sun protection.",
    },
    6: {
        1: "Dehydrated skin. Drink more water & use hyaluronic acid.",
        2: "Use moisturizing serums.",
        3: "Keep your hydration routine.",
        4: "Maintain hydrating care.",
        5: "Excellent hydration. Keep it up!",
    },
    7: {
        1: "No spots. Maintain tone.",
        2: "Few spots. Try vitamin C.",
        3: "Some pigmentation. Use niacinamide.",
        4: "Moderate spots. Add alpha arbutin.",
        5: "Severe pigmentation. Consult expert.",
    },
    8: {
        1: "Very tight skin. Use rich cream.",
        2: "Slight tightness. Apply serum regularly.",
        3: "Balanced feel. Continue current care.",
        4: "No tightness. Skin feels fine.",
        5: "Loose skin. Consider firming treatments.",
    },
    9: {
        1: "No skincare. Start simple: cleanser + moisturizer.",
        2: "Rare use. Add sunscreen.",
        3: "Decent care. Improve consistency.",
        4: "Good routine. Add serum if needed.",
        5: "Excellent care. You're doing great!",
    }
}
def quiz_view(request):
    if request.method == 'POST':
        answers = [request.POST.get(f'q{i}') for i in range(10)]
        if None in answers:
            return render(request, 'quiz.html', {
                'questions': zip(range(10), QUESTIONS),
                'options': OPTIONS,
                'error': "Please answer all questions."
            })

        scores = [SCORE_MAP[a] for a in answers]
        recommendations = [
            RECOMMENDATIONS[i][score] for i, score in enumerate(scores)
        ]
        return render(request, 'result.html', {
                'recommendations': zip(QUESTIONS, recommendations)
            })
    return render(request, 'quiz.html', {
        'questions': zip(range(10), QUESTIONS),
        'options': OPTIONS
    })