from django.shortcuts import get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from products.models import Product, Rating
from .models import BrowsingHistory

@login_required
def product_interaction(request, product_id):
    """
    ثبت تعامل کاربر با محصول:
    view, cart, wishlist, like, rating
    """
    product = get_object_or_404(Product, id=product_id)
    action = request.POST.get('action')  # view, cart, wishlist, like, rating

    # ثبت interaction تو BrowsingHistory
    BrowsingHistory.objects.create(
        user=request.user,
        product=product,
        interaction_type=action
    )

    # اگر action ریتینگ بود، مقدار ریتینگ رو هم از فرم بگیر و تو مدل Rating ذخیره کن
    if action == "rating":
        rating_value = int(request.POST.get('rating', 0))
        # ثبت یا آپدیت ریتینگ
        Rating.objects.update_or_create(
            user=request.user,
            product=product,
            defaults={'value': rating_value}
        )

        # اگر ریتینگ بالای 3 بود → Like و Wishlist هم ثبت کن
        if rating_value > 3:
            BrowsingHistory.objects.get_or_create(
                user=request.user,
                product=product,
                interaction_type="like"
            )
            BrowsingHistory.objects.get_or_create(
                user=request.user,
                product=product,
                interaction_type="wishlist"
            )

    return JsonResponse({'status': 'success'})
