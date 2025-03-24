from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name = 'main'

urlpatterns = [
    path('<slug:slug>/', views.PostListView.as_view(), name="post_list"),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name="post_single"),
    path('comment/<int:pk>', views.CreateComment.as_view(), name="comment"),
    path('', views.HomeView.as_view(), name='main'),

]

