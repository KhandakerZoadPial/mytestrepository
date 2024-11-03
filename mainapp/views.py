from django.shortcuts import render


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def home(request):
    return render(request, 'mainapp/home.html')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def authenticated_view(request):
    return Response({'message': 'Success! You are authenticated.'}, status=status.HTTP_200_OK)