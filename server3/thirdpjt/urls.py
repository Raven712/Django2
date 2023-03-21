"""thirdpjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
# from practices import views as practices_views
# from practices2  import views as practices2_views
#앱이 여러개가 되어 views가 겹치니까 별칭인 as를 사용한다! (방법 1)

# include를 추가해줘야 각 앱마다 만들어둔 urls.py와 상호작용이 된다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('practices/', include('practices.urls')),
    path('practices2/', include('practices2.urls')),
    # path('', practices2_views.index),
    # practices2는 방명록 기능 (저장)
]
