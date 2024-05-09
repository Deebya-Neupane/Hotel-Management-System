from urllib import response
from django.shortcuts import render
from rest_framework import generics, status
from .models import Feedback
from .serializers import FeedbackSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import CustomModelPermission


# Create your views here.
class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated, CustomModelPermission]

    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        if user_id:
            serializer.save(user_id=user_id)
        else:
            return response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)