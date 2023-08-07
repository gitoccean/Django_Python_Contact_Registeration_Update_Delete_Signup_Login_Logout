from django import forms
from project.models import SignupModel,SigninModel,RegisterModel


class SignupForm(forms.ModelForm):
    class Meta:
        model = SignupModel
        fields= '__all__'

    def clean(self):
        cd = self.cleaned_data
        if cd.get('Password') != cd.get('Confirm_Password'):
            self.add_error('Confirm_Password', "passwords do not match !")
        return cd



class SigninForm(forms.Form):
    Username= forms.CharField(max_length=20)
    Password= forms.CharField(max_length=30)

 


class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterModel
        fields= '__all__'        



class DataForm(forms.Form):
    name = forms.CharField(max_length=30)
    email= forms.EmailField()
    phone= forms.IntegerField()
    city = forms.CharField()
    province= forms.CharField()
    country= forms.CharField()

    def __str__(self):
        return self.name

