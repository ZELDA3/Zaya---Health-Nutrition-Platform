from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage),
    path("about/", views.AboutUs),
    path("sign-up/", views.SignUpView.as_view()),
    path("plans/", views.NutritionPlanListView.as_view()),
    path("profile/", views.ProfileCreateView.as_view()),
    path("profile/detail/<int:pk>/", views.ProfileDetailView.as_view()),
    path("profile/update/<int:pk>/", views.ProfileUpdateView.as_view()),
    path("profile/delete/<int:pk>/", views.ProfileDeleteView.as_view()),
]
