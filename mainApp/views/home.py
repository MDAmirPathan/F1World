import logging

from django.shortcuts import render, HttpResponse


logger = logging.getLogger("django")
# Create your views here.

def home(request):
    logger.info("hi")
    return render(request, 'home.html')