from rest_framework import viewsets , status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import StudentData1
from .serializers import StudentSerializer , MarksSerializer , StudentDBTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class StudentViewSet (viewsets.ReadOnlyModelViewSet):
    queryset = StudentData1.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return super().get_serializer_class()
    

    def update_marks (self , request , pk = None):
        student = self.get_object()

        serializer = MarksSerializer(student , data=request.data , partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(self.get_serializer_class(student).data)
        
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    

class StudentDBTokenView(TokenObtainPairView):
    serializer_class = StudentDBTokenSerializer