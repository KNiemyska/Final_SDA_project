from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from appcat.models import Gear

posty_na_bloga = [
    {'author': "Kasia",
     "title": "blog1",
     "content": "treść bloga 1",
     'date_posted': 'data posta'
     },
    {'author': "Tomek",
     "title": "blog2",
     "content": "treść bloga 2",
     'date_posted': "data posta 2"
     }

]

class MainView(View):
    template = 'appcat/home.html'
    posty_na_bloga = [
            {'author': "Kasia",
             "title": "blog1",
             "content": "treść bloga 1",
             'date_posted': 'data posta'
             },
            {'author': "Tomek",
             "title": "blog2",
             "content": "treść bloga 2",
             'date_posted': "data posta 2"
             }

        ]
    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        context = {
            'posty_na_bloga': self.posty_na_bloga
        }
        return render(request, self.template, context)

def home(request):
    context = {
        'posty_na_bloga': posty_na_bloga
    }
    return render(request, 'appcat/home.html', context)

def about(request):

    return render(request,'appcat/about.html', {"title":"TYTUŁ Z ABOUT"})