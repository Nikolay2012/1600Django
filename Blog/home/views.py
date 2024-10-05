from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main_page(request):
#   return HttpResponse("Hello your on a home page")
    return render(request= request, template_name= "home/home.htm")