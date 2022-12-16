from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class ContactForm(forms.Form):
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control'}))