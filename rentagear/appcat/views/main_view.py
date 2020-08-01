from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
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

class PostListView(ListView):
    model= Gear
    template_name = 'appcat/home.html'
    context_object_name = 'gears'
    ordering = ['-date_posted'] #to order view of posts
# <app>/<model>_<viewtype>.html
def about(request):

    return render(request,'appcat/about.html', {"title":"TYTUŁ Z ABOUT"})