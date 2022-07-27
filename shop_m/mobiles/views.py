from django.shortcuts import render
from .models import main_images
from .models import Top_Models


def index(request):
    gl_img_verj = main_images.objects.filter(position1=True)
    gl_img_niz = main_images.objects.filter(position2=True)

    top_model_im1 = Top_Models.objects.filter(show_art1=True)
    top_model_im2 = Top_Models.objects.filter(show_art2=True)
    return render(request, 'index.html', {'image_top': gl_img_verj, 'image_bot': gl_img_niz, 'top_model_image1' : top_model_im1,
                                          'top_model_image2' : top_model_im2})

def test(request):
    gl_img_verj = main_images.objects.filter(position1=True)
    gl_img_niz = main_images.objects.filter(position2=True)

    top_model_im1 = Top_Models.objects.filter(show_art1=True)
    return render(request, 'test.html', {'image_top': gl_img_verj, 'image_bot': gl_img_niz, 'top_model_image1' : top_model_im1})
