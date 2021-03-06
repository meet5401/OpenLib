from django.urls import path, include
from rest_framework import routers


from . import views

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register('', views.BooksViewSet)
router.register('uploadBook/', views.BooksViewSet)

urlpatterns = [
    path("login/", views.signin, name="login"),
    path("user/createUser/", views.signup, name="signup"),
    path("logout/<int:id>/", views.signout, name="logout"),


    path("", include(router.urls), name="see up at the 'router'"),
    path("addBook/<str:id>/<str:token>/",
         views.addBook, name="add a new book"),
    path("<int:bookId>/<str:id>/<str:token>/removeBook/",
         views.removeBook, name="remove a book"),

    path("<int:bookId>/<str:action>/",
         views.perfromActionOnBook, name="Upvoting book")  # NOTE: LIKE, UNLIKE TODO: Report

]
