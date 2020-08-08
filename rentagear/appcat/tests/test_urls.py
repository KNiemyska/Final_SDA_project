from django.test import SimpleTestCase
from django.urls import reverse, resolve
from appcat.views.main_view import PostListView, \
    PostDetailView,\
    PostCreateView,\
    PostDeleteView,\
    PostUpdateView

class TestUrls(SimpleTestCase):
    def test_home_home_url_is_resolves(self):
        url=reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class,PostListView)

    def test_create_view_url_is_resolves(self):
        url = reverse('gear-create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_detail_view_url_is_resolves(self):
        url = reverse('gear-detail',args=['75194d3-6885-417e-a8a8-6c931e272f00'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDetailView)
    def test_update_view_url_is_resolves(self):
        url = reverse('gear-update', args=['75194d3-6885-417e-a8a8-6c931e272f00'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_delete_view_url_is_resolves(self):
        url = reverse('gear-delete', args=['75194d3-6885-417e-a8a8-6c931e272f00'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)