from django import forms
from .models import Tution ,Application

class add_psot(forms.ModelForm):
    class Meta:
        model = Tution
        # fields = '__all__'
        exclude=['author']

class ApplicatioForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["tution"]