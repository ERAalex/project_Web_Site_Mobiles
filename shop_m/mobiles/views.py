from django.shortcuts import render
from django.core.paginator import Paginator
from .models import main_images
from .models import Top_Models
from .models import all_products
from .forms import LoginForm, UserRegistrationForm
from django.views.generic import DetailView



def index(request):
    gl_img_verj = main_images.objects.filter(position1=True)
    gl_img_niz = main_images.objects.filter(position2=True)

    top_model_im1 = Top_Models.objects.filter(show_art1=True)
    top_model_im2 = Top_Models.objects.filter(show_art2=True)
    return render(request, 'index.html', {'image_top': gl_img_verj, 'image_bot': gl_img_niz, 'top_model_image1' : top_model_im1,
                                          'top_model_image2' : top_model_im2})


def products(request):
    all_products_show = all_products.objects.all()
    return render(request, 'products.html', {'all_products_show': all_products_show})



###### блок ссылок и вьюшек для вывода конкретных моделей внутри шаблона products

def apple_show(request):
    all_products_show = all_products.objects.filter(show_apple=True)
    return render(request, 'products.html', {'all_products_show': all_products_show})

def samsung_show(request):
    all_products_show = all_products.objects.filter(show_samsung=True)
    return render(request, 'products.html', {'all_products_show': all_products_show})

def huawei_show(request):
    all_products_show = all_products.objects.filter(show_huawei=True)
    return render(request, 'products.html', {'all_products_show': all_products_show})

def chip_show(request):
    all_products_show = all_products.objects.all().order_by('price')
    return render(request, 'products.html', {'all_products_show': all_products_show})

def expensive_show(request):
    all_products_show = all_products.objects.all().order_by('price').reverse()
    return render(request, 'products.html', {'all_products_show': all_products_show})
######


###### вывод каждого товара на отдельной странице через DetailView (если что, подробно все описал в WORD ищи в теории

class ProductDeatailView(DetailView):
    model = all_products
    template_name = 'product_show.html'
    context_object_name = 'product_see'
######

###### Пагинация всех товаров на странице product

def prod_list(request, page_numb = 1):
    product_pagin = all_products.objects.all()
    current_page = Paginator(product_pagin, 3)  # 3 posts in each page
    return render(request, 'products.html', {'current_page': current_page.page(page_numb)})

######



def test(request):
    gl_img_verj = main_images.objects.filter(position1=True)
    gl_img_niz = main_images.objects.filter(position2=True)

    top_model_im1 = Top_Models.object.filter(show_art1=True)
    return render(request, 'test.html', {'image_top': gl_img_verj, 'image_bot': gl_img_niz, 'top_model_image1' : top_model_im1})



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
