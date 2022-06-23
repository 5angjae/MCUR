from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer


import requests
# Create your views here.

@api_view(['POST'])
def movie_create(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(data=serializer.data)

def movie_arrange(movie):
    api_key = 'daeb2caee9f1ae379dd6777405783a00'
    tmdb_data = {'pk':movie.pk}
    if movie.type == "movie":
        url_kr = f'https://api.themoviedb.org/3/movie/{movie.tmdb_id}?api_key={api_key}&language=ko-KR'
        url = f'https://api.themoviedb.org/3/movie/{movie.tmdb_id}?api_key={api_key}'
        res_kr = requests.get(url_kr)
        movie_data = res_kr.json()

        tmdb_data["title"] = movie_data["title"]
        tmdb_data["release_date"] = movie_data["release_date"]
        tmdb_data["original_title"] = movie_data["original_title"]
        tmdb_data["tmdb_id"] = movie_data["id"]
        tmdb_data["overview"] = movie_data["overview"]


    elif movie.type == "tv":
        url_kr = f'https://api.themoviedb.org/3/tv/{movie.tmdb_id}?api_key={api_key}&language=ko-KR'
        url = f'https://api.themoviedb.org/3/tv/{movie.tmdb_id}?api_key={api_key}'
        res_kr = requests.get(url_kr)
        tv_data = res_kr.json()

        tmdb_data["title"] = tv_data["name"]
        tmdb_data["release_date"] = tv_data["first_air_date"]
        tmdb_data["original_title"] = tv_data["original_name"]
        tmdb_data["tmdb_id"] = tv_data["id"]
        tmdb_data["overview"] = tv_data["overview"]

    tmdb_data["poster_path"] = requests.get(url).json()["poster_path"]
    tmdb_data["backdrop_path"] = requests.get(url).json()["backdrop_path"]
    tmdb_data["heros"] = movie.heros.split(' / ')
    tmdb_data["cookie_movie_id"] = movie.cookie_movie_id
    
    return tmdb_data
    

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    movie_list = []
    for movie in movies:
        movie_list.append(movie_arrange(movie))
    
    return Response(movie_list)

# @api_view(['GET'])
# def hero_movie_list(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     movies = Movie.objects.all()
#     recommend_movies = {}
#     for hero in movie_arrange(movie)["heros"]:
#         recommend_movies[f'{hero}'] = []
#         for mov in movies:
#             if mov.pk == movie_pk:
#                 pass
#             else:
#                 if hero in movie_arrange(mov)["heros"]:
#                     recommend_movies[f'{hero}'].append(mov)
#     print(recommend_movies)
    
#     return recommend_movies

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    return Response(movie_arrange(movie))



@api_view(['GET'])
def review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = Review.objects.filter(movie_id=movie_pk)
    serializers = ReviewSerializer(reviews, many=True)
    return Response(serializers.data)
    
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_login(request, movie_pk):
    reviews = Review.objects.filter(movie_id=movie_pk)
    serializers = ReviewSerializer(reviews, many=True)
    login_review_list = []

    for serializer in serializers.data:
        
        serial = dict(serializer)
        
        if request.user.user_reviews.filter(movie=movie_pk).exists():
            print(request.user.user_reviews.filter(movie=movie_pk).values()[0])
            print(serial)
            if request.user.user_reviews.filter(movie=movie_pk).values()[0]['user_id'] == serial['user']:
                pass
            else:
                login_review_list.append(serial)
        else:
            login_review_list.append(serial)
    
    return Response(login_review_list)
    #     if serial == request.user.user_reviews.filter(movie=movie_pk).values():
    #         print(serial)
    #         login_review_list.append(serial)
    # if request.user.user_reviews.filter(movie=movie_pk).exists():
    #     print(dict(serializers.data))
    #     print(request.user.user_reviews.filter(movie=movie_pk).values())
    #     new_review_list = serializers.data.values() - request.user.user_reviews.filter(movie=movie_pk).values()[0]
    #     return new_review_list
    # else:
    #     return Response(serializers.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend_list_rate(request):
    appeared_movie = {}
    movies = Movie.objects.all()
    
    for movie in movies:
        for hero in movie.heros.split(' / '):
            if hero in appeared_movie.keys():
                appeared_movie[hero] += 1
            else:
                appeared_movie[hero] = 1

    recommend_hero = {}
    serializers = ReviewSerializer(request.user.user_reviews, many=True)
    
    watch_list = []
    for serializer in serializers.data:
        serial = dict(serializer)
        watch_list.append(serial['movie'])
        if serial['rank'] >= 7:
            movie = get_object_or_404(Movie, pk=serial['movie'])
            for hero in movie.heros.split(' / '):
                if hero in recommend_hero.keys():
                    recommend_hero[hero] += 1
                else:
                    recommend_hero[hero] = 1
    max_hero_rate = 0
    max_hero = ''
    for hero in recommend_hero.keys():
        hero_rate = recommend_hero[hero] / appeared_movie[hero]
        
        if max_hero_rate < hero_rate < 1 and appeared_movie[hero] >= 5:
            max_hero_rate = hero_rate
            max_hero = hero

    recommend_list = []    
    for movie in movies:
        if max_hero in movie.heros.split(' / '):
            if movie.pk not in watch_list:
                recommend_list.append(movie.pk)
    
    recommend_movie_list = ['who?']
    for recommend in recommend_list:
        movie = get_object_or_404(Movie, pk=recommend)
        recommend_movie_list.append(movie_arrange(movie))
    
    recommend_movie_list[0] = max_hero
    return Response(recommend_movie_list)
    

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    # 1. 해당 review의 유저가 아닌 경우, review를 수정하거나 삭제하지 못하게 설정
    if not request.user.user_reviews.filter(pk=review_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)


    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            review_data = serializer.data
            review_data['id'] = review.id
            return Response(review_data)

    elif request.method == 'DELETE':
        review.delete()

        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_movie_review(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.user_reviews.filter(movie=movie_pk).exists():
        print(request.user.user_reviews.filter(movie=movie_pk))
        return Response(request.user.user_reviews.filter(movie=movie_pk).values())
        
    else:
        return Response({'my_review':'True'})
