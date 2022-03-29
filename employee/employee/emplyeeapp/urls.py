from . import views
from django.urls import path
app_name='emplyeeapp'

urlpatterns = [
    path('', views.fn_home, name='fn_home'),
    path('register/',views.fn_register, name='fn_register'),
    path('add/',views.fn_add, name='fn_add'),
    path('login/',views.fn_login, name='fn_login'),
    path('emplogin/',views.fn_Emplogin,name='fn_Emplogin'),
    path('logout',views.fn_logout, name='fn_logout'),
    path('emplist',views.fn_emplist, name='fn_emplist'),
    path('view/<int:empid>/',views.fn_view,name='view')

]