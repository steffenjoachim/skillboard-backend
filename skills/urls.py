from django.urls import path
from .views import SkillListCreateView, RegisterView, CategoryListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("skills/", SkillListCreateView.as_view(), name="skill-list"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
