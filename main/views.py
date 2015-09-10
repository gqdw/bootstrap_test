from django.shortcuts import render
from django import forms
# Create your views here.
class Testform(forms.Form):
	user = forms.CharField(max_length=30)
	password = forms.CharField(max_length=30)
	

def index( request ):
	f = Testform()
	return render(request , 'index.html',{'form':f})
