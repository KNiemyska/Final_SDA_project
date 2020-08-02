from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from appcat.models import Gear, Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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
    model = Gear
    template_name = 'appcat/home.html'
    context_object_name = 'gears'
    ordering = ['-date_posted']  # to order view of posts


# <app>/<model>_<viewtype>.html

class PostDetailView(DetailView):
    model = Gear


# will look automaticly for such template <app>/<model>_<viewtype>.html, this is why we dont need to specify this

class PostCreateView(LoginRequiredMixin, CreateView):  # to create new post
    # i want that only login users can creaate posts but we cant use decorator, for
    # this i will use LoginRequiredMixin class
    model = Gear
    fields = ['title', 'year_of_production', 'content', 'picture']

    def form_valid(self, form):  # the author of post will be logged person
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # to create new post
    # i want that only login users can creaate posts but we cant use decorator, for
    # this i will use LoginRequiredMixin class
    # i want only author of the post can update theirs post- i will use UsersPassesTestMixin

    model = Gear
    fields = ['title', 'year_of_production', 'content', 'picture']

    def form_valid(self, form):  # the author of post will be logged person
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(
            self):  # this function will be use by UserPassesTestMixin to find if post is updated by user who created this
        # we want get curently post that we are updating
        gear = self.get_object()
        if self.request.user == gear.author:  # this get current login user and chcecking if this is author of post
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # we want the user to be login and the user is author of the post -> we will use the same functionality as in PostUpdateView
    model = Gear
    success_url = '/'  # where to redirect if gear is deleted?

    def test_func(self):
        gear = self.get_object()
        if self.request.user == gear.author:
            return True
        return False


def about(request):
    return render(request, 'appcat/about.html', {"title": "TYTUŁ Z ABOUT"})
