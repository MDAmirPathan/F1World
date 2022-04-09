import logging

from django.shortcuts import render, HttpResponse


logger = logging.getLogger("django")
# Create your views here.


def home(request):
    logger.info("hi")
    return render(request, 'home.html')


def aboutUS(request):
    logger.info("hi")
    return render(request, 'about-us.html')


def contactUS(request):
    logger.info("hi")
    return render(request, 'contact-us.html')


def results(request):
    logger.info("hi")
    return render(request, 'results.html')


def standings(request):
    logger.info("hi")
    return render(request, 'standings.html')


def whatsNew(request):
    logger.info("hi")
    return render(request, 'whats-new.html')


def liveTiming(request):
    logger.info("hi")
    return render(request, 'live-timing.html')
