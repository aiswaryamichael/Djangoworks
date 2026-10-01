from http.client import HTTPResponse

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#function based

# def Home(request):
#     if(request.method=="GET"):
#         return HttpResponse("welcome to Django")
#
#
# #define index view returns message "index page"
#
# def Index(request):
#     if(request.method=="GET"):
#         return HttpResponse("index page")

#class based

from django.views import View

class Home(View):
    def get(self,request):

        return HttpResponse("welcome to Django")


#define index view returns message "index page"

class Index(View):
    def get(self,request):
        return HttpResponse("index page")