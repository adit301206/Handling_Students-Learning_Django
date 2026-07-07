from rest_framework import viewsets , status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StudentData1
from .serializers import StudentSerializer

class StudentViewSet (viewsets.ReadOnlyModelViewSet):
    queryset = StudentData1.objects.all()
    serializer_class = StudentSerializer
    permission_classes = []

    def get_serializer_class(self):
        return super().get_serializer_class()
    

    def update_marks (self , request , pk = None):
        student = self.get_object()