from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
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

class PostDetailView(DetailView):
    model= Gear

# will look automaticly for such template <app>/<model>_<viewtype>.html, this is why we dont need to specify this

class PostCreateView(CreateView): #to create new post
    model= Gear
    fields=['title','picture','content']

    def form_valid(self,form): #the author of post will be logged person
        form.instance.author=self.request.user
        return super().form_valid(form)

def about(request):

    return render(request,'appcat/about.html', {"title":"TYTUŁ Z ABOUT"})