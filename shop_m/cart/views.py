from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from mobiles.models import all_products
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(all_products, id= product_id)
    # для работы с корзиной используем нашу форму
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product= product,
                 quantity= cd['quantity'],
                 update_quantity= cd['update'])
    # в конце перенаправляем пользователя -redirect- на страницу(url cart_detail)
    return redirect('cart:cart_detail')



def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(all_products, id= product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


