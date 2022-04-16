from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class Anime_API(APIView):

    def get(self, request, pk=''):
        print(pk)
        if pk == '':
            _Anime = Anime.objects.all()

            serializer = AnimeSerializer(_Anime, many=True)

            return Response(serializer.data)
        else:
            _Anime = Anime.objects.get(id=pk)
            serializer = AnimeSerializer(_Anime)
            return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = AnimeSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print(request.data[0])

        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        _Anime = Anime.objects.get(id=pk)
        serializer = AnimeSerializer(_Anime, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        _Anime = Anime.objects.get(id=pk)
        _Anime.delete()
        return Response({"msg": "Apagado com sucesso"})

class Category_API(APIView):

    def get(self, request, pk=''):
        print(pk)
        if pk == '':
            _Category = Category.objects.all()

            serializer = CategorySerializer(_Category, many=True)

            return Response(serializer.data)
        else:
            _Category = Category.objects.get(id=pk)
            serializer = CategorySerializer(_Category)
            return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = CategorySerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print(request.data[0])

        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        _Category = Category.objects.get(id=pk)
        serializer = CategorySerializer(_Category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        _Category = Category.objects.get(id=pk)
        _Category.delete()
        return Response({"msg": "Apagado com sucesso"})

class SeasonGroup_API(APIView):

    def get(self, request, pk=''):
        print(pk)
        if pk == '':
            _SeasonGroup = SeasonGroup.objects.all()

            serializer = SeasonGroupSerializer(_SeasonGroup, many=True)

            return Response(serializer.data)
        else:
            _SeasonGroup = SeasonGroup.objects.get(id=pk)
            serializer = SeasonGroupSerializer(_SeasonGroup)
            return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = SeasonGroupSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print(request.data[0])

        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        _SeasonGroup = SeasonGroup.objects.get(id=pk)
        serializer = SeasonGroupSerializer(_SeasonGroup, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        _SeasonGroup = SeasonGroup.objects.get(id=pk)
        _SeasonGroup.delete()
        return Response({"msg": "Apagado com sucesso"})

class EpsGroup_API(APIView):

    def get(self, request, pk=''):
        print(pk)
        if pk == '':
            _EpsGroup = EpsGroup.objects.all()

            serializer = EpsGroupSerializer(_EpsGroup, many=True)

            return Response(serializer.data)
        else:
            _EpsGroup = EpsGroup.objects.get(id=pk)
            serializer = EpsGroupSerializer(_EpsGroup)
            return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = EpsGroupSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print(request.data[0])

        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        _EpsGroup = EpsGroup.objects.get(id=pk)
        serializer = EpsGroupSerializer(_EpsGroup, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        _EpsGroup = EpsGroup.objects.get(id=pk)
        _EpsGroup.delete()
        return Response({"msg": "Apagado com sucesso"})

class Episode_API(APIView):

    def get(self, request, pk=''):
        print(pk)
        if pk == '':
            _Episode = Episode.objects.all()

            serializer = EpisodeSerializer(_Episode, many=True)

            return Response(serializer.data)
        else:
            _Episode = Episode.objects.get(id=pk)
            serializer = CategorySerializer(_Episode)
            return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = EpisodeSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print(request.data[0])

        return Response({"msg": "Inserido com sucesso"})

    def put(self, request, pk=''):
        _Episode = Episode.objects.get(id=pk)
        serializer = EpisodeSerializer(_Episode, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        _Episode = Episode.objects.get(id=pk)
        _Episode.delete()
        return Response({"msg": "Apagado com sucesso"})