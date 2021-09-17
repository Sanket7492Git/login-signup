from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label = 'Confirm Password (again)', widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email': 'Email'}

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name' , 'email', 'date_joined' , 'last_login'] 
        labels = {'email' : 'Email'}


# here all the fiels will be shown in the form which are given in the fields
# password and confirm password will also be shown even if it is not given in the field because both the fields are part of user creation form while other fields are part of form which is created by user (in this case it is SignUpForm)