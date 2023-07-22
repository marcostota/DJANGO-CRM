from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("record/<int:pk>", views.customer_record, name="record"),
    path("delete_record/<int:pk>", views.delete_customer, name="delete_record"),
    path("add_customer", views.add_customer, name="add_customer"),
    path("update_record/<int:pk>", views.update_customer, name="update_customer"),
]
# urlpatterns = [path("login/", views.login_user, name="login")]
