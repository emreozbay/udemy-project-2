from django import forms
from django.core import validators
from basicapp.models import Users, UserProfileInfo
from  django.contrib.auth.models import User


#def check_for_z(value):
 #   if value[0].lower() != 'z':
  #      raise forms.ValidationError("Name Needs To Start With Z")

class FormName(forms.Form):
    name =forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter Your email again')
    text =forms.CharField(widget=forms.Textarea)
   # botcatcher =forms.CharField(required=False,widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make Sure Emails Match")



class NewUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


