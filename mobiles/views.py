from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import main_images
from .models import all_products, Articles
from .forms import LoginForm, UserRegistrationForm
from django.views.generic import DetailView
from cart.forms import CartAddProductForm
from .email_code import email_check



def index(request):
    # блок отправки письма
    form = email_check(request)

    all_result = all_products.objects.filter(show_on_main_page=True)
    gl_img_verj = main_images.objects.filter(position1=True)
    gl_img_niz = main_images.objects.filter(position2=True)

    cart_product_form = CartAddProductForm()

    return render(request, 'index.html', {
        'all_result': all_result,
        'image_top': gl_img_verj,
        'image_bot': gl_img_niz,
        'cart_product_form': cart_product_form,
        'form': form
    })



def apple_show(request):
    all_products_show = all_products.objects.filter(show_apple=True)
    return render(request, 'products.html', {'all_products_show': all_products_show})


def samsung_show(request):
    all_products_show = all_products.objects.filter(show_samsung=True)
    return render(request, 'products.html', {'all_products_show': all_products_show})


def huawei_show(request):
    all_products_show = all_products.objects.filter(show_huawei=True)
    return render(request, 'products.html', {'all_products_show': all_products_show})


def honor_show(request):
    all_products_show = all_products.objects.filter(show_honor=True)
    return render(request, 'products.html', {'all_products_show': all_products_show})


def chip_show(request):
    all_products_show = all_products.objects.all().order_by('price')
    return render(request, 'products.html', {'all_products_show': all_products_show})


def expensive_show(request):
    all_products_show = all_products.objects.all().order_by('price').reverse()
    return render(request, 'products.html', {'all_products_show': all_products_show})


def discount_show(request):
    discount_products = all_products.objects.all().filter(discount_active=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product_show.html', {'discount_products': discount_products,
                                                 'cart_product_form': cart_product_form})


# Для корзины.
def product_detail(request, id):
    product = get_object_or_404(all_products, id=id, show_item=True)
    cart_product_form = CartAddProductForm()
    # путь до другого шаблона (не cart)
    return render(request, 'shop_m/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
#

# Вывод при нажатии продукта на отдельной странице
class ProductDeatailView(DetailView):
    model = all_products
    template_name = 'product_show.html'
    context_object_name = 'product_see'


# Пагинация всех товаров на странице product
def prod_pag_page(request):
    try:
        pag_prod = all_products.objects.all()
        if 'page' in request.GET:
            page = request.GET['page']
        else:
            page = 1
        paginator = Paginator(pag_prod, 6)
        try:
            pag_prod = paginator.page(page)
        except PageNotAnInteger:
            pag_prod = paginator.page(1)
        except EmptyPage:
            pag_prod = paginator.page(paginator.num_pages)

        cart_product_form = CartAddProductForm()
        gl_img_verj = main_images.objects.filter(position1=True)

        context = {'pag_prod': pag_prod,
                   'cart_product_form': cart_product_form,
                   'image_top': gl_img_verj,
                   }
        return render(request, "products.html", context)
    except:
        return render(request, "products.html")


def insurance(request):
    return render(request, 'insurance.html')

def company(request):
    all_company = Articles.objects.filter(company_article=True, show_item=True)
    return render(request, 'company.html', {'all_company': all_company})

def contact(request):
    contact = Articles.objects.filter(show_item=True, title='Контактный центр: 8 800 245 45 25')
    return render(request, 'contact.html', {'contact': contact})


# Форма регистрации пользователя
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/registr_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/registr.html', {'user_form': user_form})
