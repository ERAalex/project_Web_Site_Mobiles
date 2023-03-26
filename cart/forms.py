from django import forms

# ниже будет находиться количество выбранного товара (от 1 до 20)
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


# форма для добавления товара в корзину
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)