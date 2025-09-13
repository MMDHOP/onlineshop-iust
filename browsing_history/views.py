from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from collections import defaultdict

from products.models import Product, Ratings
from .models import BrowsingHistory


@login_required
def product_interaction(request, product_id):
    product = get_object_or_404(Product, id=product_id)


    BrowsingHistory.objects.get_or_create(
        user=request.user,
        product=product,
        interaction_type="view"
    )


    all_histories = BrowsingHistory.objects.filter(user=request.user).order_by('-timestamp')
    product_histories = defaultdict(list)
    for h in all_histories:
        if h.interaction_type not in product_histories[h.product]:
            product_histories[h.product].append(h.interaction_type)

    return render(request, 'browsing_history.html', {
        'product_histories': dict(product_histories)
    })


@login_required
def browsing_history_view(request):
    all_histories = BrowsingHistory.objects.filter(user=request.user).order_by('-timestamp')
    
    product_histories = defaultdict(list)
    product_last_view = {} 

    for h in all_histories:
        if h.interaction_type not in product_histories[h.product]:
            product_histories[h.product].append(h.interaction_type)
        
        if h.product not in product_last_view:
            product_last_view[h.product] = h.timestamp
            
    histories_with_time = [
        {'product': product, 'interactions': interactions, 'last_view': product_last_view[product]}
        for product, interactions in product_histories.items()
    ]

    return render(request, 'browsing_history.html', {
        'histories_with_time': histories_with_time,
    })




@login_required
def clear_browsing_history(request):
    if request.method == "POST":
        BrowsingHistory.objects.filter(user=request.user).delete()
        messages.success(request, "Browsing history cleared!")
    return redirect('browsing_history')
