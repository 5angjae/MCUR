from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.movie_create, name='movie_create'),
    path('index/', views.movie_list, name='movie_list'),
    path('<int:movie_pk>/', views.movie_detail,  name='movie_detail'),
    # path('<int:movie_pk>/recommend/', views.hero_movie_list, name='hero_movie_list'),
    path('<int:movie_pk>/reviews/', views.review_list,  name='review_list'),
    path('<int:movie_pk>/reviews2/', views.review_list_login,  name='review_list_login'),
    path('<int:movie_pk>/review/create/', views.review_create, name='review_create'),
    path('review/<int:review_pk>/', views.review_update_delete, name='review_update_delete'),
    path('rlr/', views.recommend_list_rate, name='recommend_list_rate'),
    path('<int:movie_pk>/my_review/', views.my_movie_review, name='my_movie_review')
]
