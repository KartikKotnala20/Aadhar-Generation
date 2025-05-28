from django import forms
from .models import Aadhar

class AadharForm(forms.ModelForm):
    
    class Meta:
        model = Aadhar
        fields = [ 'first_name','last_name','father_name','mother_name',
                    'dob','address','state','pincode','phone','mail',
                    'aadhar_num','gender','photo'
        ]
