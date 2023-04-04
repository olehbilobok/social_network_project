"""social_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.views import UserRegistration, UserActivityViewDetail, UserActivityViewList, LogoutView
from post.views import POSTList, LikeDetail, AnalyticsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/register', UserRegistration.as_view(), name="register"),
    path('api/post', POSTList.as_view(), name="get_post"),
    path('api/post/<int:pk>/like', LikeDetail.as_view(), name="like_unlike"),
    path('api/analytics', AnalyticsView.as_view(), name="analytics"),
    path('api/logout', LogoutView.as_view(), name="logout"),
    path('api/user/<int:pk>/activity', UserActivityViewDetail.as_view(), name="activity"),
    path('api/user/activity', UserActivityViewList.as_view(), name="activity_all")

]
