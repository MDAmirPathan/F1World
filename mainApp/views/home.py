import logging
import time
import os
from pathlib import Path
from django.shortcuts import render, HttpResponse
import fastf1

logger = logging.getLogger("django")
# Create your views here.


def home(request):

    return render(request, 'home.html')

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_calculate_t0_date', '_car_data', '_check_lap_accuracy', '_drivers_from_f1_api', '_drivers_results_from_ergast', '_get_property_warn_not_loaded', '_load_drivers_results', '_load_laps_data', '_load_telemetry', '_load_weather_data', '_pos_data', '_session_status', 'api_path', 'car_data', 'date', 'drivers', 'event', 'f1_api_support', 'get_driver', 'laps', 'load', 'load_laps', 'load_telemetry', 'name', 'pos_data', 'results', 'session_start_time', 'session_status', 't0_date', 'weather_data', 'weekend']
def aboutUS(request):
    logger.info("hi")
    return render(request, 'about-us.html')


def contactUS(request):
    logger.info("hi")
    return render(request, 'contact-us.html')


def results(request):
    # fastf1_cache_path = str(os.path.join(os.getcwd(), "static\\fastf1_cache"))
    # fastf1.Cache.enable_cache(fastf1_cache_path)
    # session = fastf1.get_session(2021, 7, 'Q')
    # session.load()
    # return render(request, 'results.html',{'session':session })
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
