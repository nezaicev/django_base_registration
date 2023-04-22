from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name',
                  'postal_code', 'city', 'phone',
                  'password1','password2',
                  )
        widgets = {
            # 'status': forms.Select(attrs={'class': 'form-select',
            #                               'onchange':'hideAdditionalInfo(this)'}),
            # 'email': forms.TextInput(attrs={'class': 'form-control ',
            #                                 'type': 'email',
            #                                 'placeholder': 'name@example.com',
            #                                 'id': 'exampleFormControlInput1',
            #                                 }),
            # 'fio':forms.TextInput(attrs={'class':'form-control',
            #                              'placeholder': 'Иванов Иван Иванович'}),
            # 'region': forms.Select(attrs={'class': 'form-select',
            #                               'onchange': 'regionChanged(this)',
            #                               'initial':1}),
            # 'district':forms.Select(attrs={'class': 'form-select',}),
            # 'city':forms.TextInput(attrs={'class': 'form-control','required':'true' }),
            # 'school': forms.TextInput(attrs={'class': 'form-control', }),
            # 'phone': forms.TextInput(attrs={'class': 'form-control' }),
            # 'position': forms.Select(attrs={'class': 'form-select', }),
            # 'age': forms.Select(attrs={'class': 'form-select'}),
            # 'subscription': forms.CheckboxInput(attrs={'class': 'custom-control custom-checkbox mb-3'}),


        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
