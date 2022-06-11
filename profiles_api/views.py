from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class ProfileView(APIView):
  '''Profile API View'''
  def get(self, request, format=None):
    an_apiview = ['User HTTP methods as function (get, post, put, patch, delete)',
                  'Is similar to a tradicional Django View',
                  'Gives you the most control over you application logic',
                  'Is mapped manually to URLs']

    return Response({'message': 'Hello!', 'an_apiview': an_apiview})
