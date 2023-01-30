from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.core.validators import RegexValidator

from testapp.models import Student_reg, Login_view, MARK, Admin_reg


class DateInput(forms.DateInput):
    input_type = 'date'

class user_register(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput,validators=[
        RegexValidator(regex='(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*\W)(?!.* ).{8,}$',message="please enter a valid password")])
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput,)
    class Meta:
        model = Login_view
        fields = ('username','password1','password2')


class Stud_Form(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)

    class Meta:
        model = Student_reg
        fields = "__all__"
        exclude = ("user",)



class Admin_Form(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)

    class Meta:
        model =  Admin_reg
        fields = "__all__"
        exclude = ("user",)


class Mark_Form(forms.ModelForm):

    class Meta:
        model = MARK
        fields = "__all__"
