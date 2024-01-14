from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('register',views.registerUser, name="register"),
    #  path('portfolio',views.portfolio, name="portfolio"),
      path('success',views.success, name="sucess_page"),
     path('portfolioForId/<int:user_id>/',views.portfolioForId, name="logout"),
]
