from django.conf.urls import url
from . import views
from .models import Posts
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^datil/(?P<post_id>[0-9]+)/', views.post_detail, name="post_detail")
]