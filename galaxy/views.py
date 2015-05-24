from django.shortcuts import render
import urllib
from urllib2 import urlopen
import requests
from urllib import urlencode

def multiform(request):
    return render(request, 'galaxy/multiform.html')
