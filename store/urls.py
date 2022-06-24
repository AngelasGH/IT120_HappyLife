from django.urls import path
from . import views


urlpatterns = [
    # user_view
    path('user_home/', views.user_home, name="user_home"),
    path('user_products/', views.user_products, name="user_products"),
    path('user_view_products/', views.user_view_products, name="user_view_products"),
    path('user_view_products_details/', views.user_view_products_details, name="user_view_products_details"),
    path('user_cart/', views.user_cart, name="user_cart"),
    path('user_checkout/', views.user_checkout, name="user_checkout"),
    path('user_faqs/', views.user_faqs, name="user_faqs"),
    path('user_about_us/', views.user_about_us, name="user_about_us"),
    path('user_contact_us/', views.user_contact_us, name="user_contact_us"),
    path('user_register/', views.user_register, name="user_register"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_reset/', views.user_reset, name="user_reset"),
    path('user_verification/', views.user_verification, name="user_user_verification"),
    path('user_reset_password/', views.user_reset_password, name="user_reset_password"),
    path('user_successfully_reset/', views.user_successfully_reset, name="user_successfully_reset"),
    path('user_reviews/', views.user_reviews, name="user_reviews"),
    # view_products
    path('user_butterfly/', views.user_butterfly, name="user_butterfly"),
    path('user_butterfly_details/', views.user_butterfly_details, name="user_butterfly_details"),
    path('user_chamomile/', views.user_chamomile, name="user_chamomile"),
    path('user_chamomile_details/', views.user_chamomile_details, name="user_chamomile_details"),
    path('user_green_tea/', views.user_green_tea, name="user_green_tea"),
    path('user_green_tea_details/', views.user_green_tea_details, name="user_green_tea_details"),
    path('user_lapsang/', views.user_lapsang, name="user_lapsang"),
    path('user_lapsang_details/', views.user_lapsang_details, name="user_lapsang_details"),

    path('update_item/', views.updateItem, name="update_item")
]

