from .models import Person
from django.forms import ModelForm, TextInput, CharField, EmailInput, EmailField, ImageField, ClearableFileInput

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ["surname","name","phone", "email", "image", "country", "city", "street"]
        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Иванов"
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Иван"
            }),
            
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "(098)-123-45-67"
            }),

            "country": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Аргентина"
            }),
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Берлин"
            }),
            
            "street": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Центральная"
            }),

            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "user@gmail.com"
            }),

            "image": ClearableFileInput(),
        }
