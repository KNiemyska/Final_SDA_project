from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from appcat.models import Gear, Post

class MainView(View):
    template = 'appcat/home.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        context = {
            'posty_na_bloga': self.posty_na_bloga
        }
        return render(request, self.template, context)

def home(request):
    context = {

        "gears": Gear.objects.all()
    }
    return render(request, 'appcat/home.html', context)

def about(request):

    return render(request,'appcat/about.html', {"title":"TYTUŁ Z ABOUT"})