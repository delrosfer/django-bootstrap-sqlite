
from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    #path('json/', views.employee_json, name="employee_json")
    path('add_contact', views.add_contact, name="add_contact"),

    path('contact/<str:contact_id>', views.contact, name="contact"),

    path('edit_contact', views.edit_contact, name="edit_contact"),

    path('delete_contact/<str:contact_id>', views.delete_contact, name="delete_contact"),

    #Login y logout

    path('login/', views.Login, name="login"), 
    path('login_user', views.LoginUser, name="login_user"), 
    path('logout/', views.LogoutUser, name="logout"), 
]
