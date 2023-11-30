from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response





@api_view(['GET','PUT','POST','PATCH'])
def index(request):
    courses = {
        "course name" : "python",
        "learn": ["flask",'dajngo','rest api'],
        "course_provider":'sclaer'}
    if request.method == 'GET':
       print('GET METHOD')
       return Response(courses)
    elif request.method == 'POST':
        print('POST METHOD')

        return Response(courses)
    