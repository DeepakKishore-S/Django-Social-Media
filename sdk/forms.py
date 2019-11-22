from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Comment



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name=forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',]


GENDER_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female'),
    ('Others', 'Others')
)


class ProfileUpdateForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, initial='Male' )
    dob = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    class Meta:
        model = Profile
        fields = ['Interested_in','Profile_image', 'gender', 'dob', 'phone']



#comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ( 'Comment',)
