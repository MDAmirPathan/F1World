from datetime import datetime

from django import template

register = template.Library()
import logging

from django.conf import settings
from django.db.models import Count, Q, Sum

logger = logging.getLogger("django")
# Function to get the total number of courses a mentor has created using the mentor ID
# @register.simple_tag
# def mentorTotalCourses(mentorID):
#     """
#     :Template Tag Function: to get the mentors total courses
#     :param: mentor ID
#     :type: int
#     :return: number of courses
#     :return type: int
#     """
#     courseQuerySet = Course.objects.filter(ruser_num=mentorID)
#     if courseQuerySet.exists():
#         courseList = list(courseQuerySet)
#         return len(courseList)
#     return 0
