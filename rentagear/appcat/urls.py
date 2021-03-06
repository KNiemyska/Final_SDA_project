from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


from appcat.views.main_view import (
    about,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView)
from users import views as user_views
from django.urls import path
from . import views
# from users.views import RegisterView

urlpatterns = [
    # path('', MainView.as_view(), name='appcat-home'),
    path('', PostListView.as_view(), name='home'),
    path('gear/new/', PostCreateView.as_view(), name='gear-create'),
    path('gear/<pk>/', PostDetailView.as_view(), name='gear-detail'),
    path('gear/<pk>/update/', PostUpdateView.as_view(), name='gear-update'),
    path('gear/<pk>/delete/', PostDeleteView.as_view(), name='gear-delete'),
    path('about/',about, name='appcat-about'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# as_view() is looking for <app>/<model>_<viewtype>.html
