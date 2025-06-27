from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Skill, Category
from .serializers import SkillSerializer, UserSerializer, CategorySerializer
from rest_framework import generics

class SkillListCreateView(APIView):
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registrierung erfolgreich!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.prefetch_related('subcategories').all()
    serializer_class = CategorySerializer