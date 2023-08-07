from django.urls import path
from project import views



urlpatterns = [
    path('home/', views.HomePage,name='home'),
    # path('home/int:id', views.HomePage, name='home-delete'),
    path("signup/",views.Signupview,name='signup'),
    # path("signupsave/",views.SignUp_save,name='signupsave'),
    path("",views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path("register/",views.RegisterPage,name='register'),
    path("register/<int:id>/",views.Register_edit,name='update'),
    path('delete/<int:id>/',views.deleteID,name='delete')

]
