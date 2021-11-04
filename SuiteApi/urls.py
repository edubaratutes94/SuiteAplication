from django.urls import path

from SuiteApi import views

urlpatterns = [

    path('login', views.LoginView.as_view()),
    path('logout', views.Logout.as_view()),
    path('registro_vivienda/list', views.RegistroViviendaList.as_view()),
    path('registro_vivienda/create', views.RegistroViviendaCreate.as_view()),
    path('registro_vivienda/<int:pk>', views.RegistroViviendaUpdate.as_view()),
    path('registro_vivienda/<int:pk>/delete', views.RegistroViviendaDelete.as_view()),


]
