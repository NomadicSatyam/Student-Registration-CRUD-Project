from django import forms
from .models import Users

# This form Project is related to Student Name And Marks Submission

class StudentRegistration(forms.ModelForm):
      class Meta:
            model = Users
            fields = ['name','email','password']
            widgets = {
                  'name':forms.TextInput(attrs={'class':'form-control'}),
                  'email':forms.EmailInput(attrs={'class':'form-control'}),
                  'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            }