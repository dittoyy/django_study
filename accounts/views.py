# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from    django.contrib.auth.forms   import  UserCreationForm 

# Create your views here.
def signup(request):                
    # return  render(request, 'signup.html')
    form    =   UserCreationForm()              
    return  render(request, 'signup.html',  {'form':    form})

