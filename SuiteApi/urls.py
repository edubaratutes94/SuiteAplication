from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers

from SuiteApi import views

urlpatterns = [

    path('register/', views.CreateUserView.as_view(), name='register'),
    path('login', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('registro_vivienda/list', views.RegistroViviendaList.as_view()),
    path('registro_vivienda/create', views.RegistroViviendaCreate.as_view()),
    path('registro_vivienda/<int:pk>', views.RegistroViviendaUpdate.as_view()),
    path('registro_vivienda/<int:pk>/delete', views.RegistroViviendaDelete.as_view()),


]
