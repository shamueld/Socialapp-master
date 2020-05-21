from .models import Server, EAI, Application
from django import forms

class ServerForm(forms.ModelForm):

    class Meta:
        model = Server     
        fields= ('name', 'os_type','environment','domain','app','eai',)    

class EAIForm(forms.ModelForm):

    class Meta:
        model = EAI      
        fields =  ('eai_code','app')

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('name', 'group')