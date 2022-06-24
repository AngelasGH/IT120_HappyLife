from django.urls import path
from . import views


urlpatterns = [
    # user_view
    path('', views.user_home, name="user_home"),
    path('user_products/', views.user_products, name="user_products"),
    path('user_cart/', views.user_cart, name="user_cart"),
    path('user_checkout/', views.user_checkout, name="user_checkout"),
    path('user_faqs/', views.user_faqs, name="user_faqs"),
    path('user_about_us/', views.user_about_us, name="user_about_us"),
    path('user_contact_us/', views.user_contact_us, name="user_contact_us"),
    path('update_item/', views.updateItem, name="update_item")
]

