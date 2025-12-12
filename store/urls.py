"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from core.views import ProductListView, ProductDetailView
from core.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core.views import CartView, AddToCartView
from core.views import PlaceOrderView, OrderHistoryView





urlpatterns = [
    path('admin/', admin.site.urls),

    # Product APIs
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    # Auth APIs
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/cart/", CartView.as_view(), name="cart-view"),
    path("api/cart/add/", AddToCartView.as_view(), name="cart-add"),
    path("api/order/place/", PlaceOrderView.as_view()),
    path("api/order/history/", OrderHistoryView.as_view()),



]

