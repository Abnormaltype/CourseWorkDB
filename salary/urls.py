from django.urls import path

from salary.views import (
    ProjectCreateView,
    ProjectListView,
    ProjectDeleteView,
    ProjectUpdateView,
    ProjectDetailView,
    WageListView,
    WageCreateView,
    WageDeleteView,
    WageDetailView,
    WageUpdateView,
    BonusListView,
    BonusCreateView,
    BonusUpdateView,
    BonusDetailView,
    BonusDeleteView,
    MainListView,
    MainDetailView,
    MainDeleteView,
    MainCreateView,
    MainUpdateView,

)

urlpatterns = [
    path("", MainListView.as_view(), name="main-list"),
    path("main-create/", MainCreateView.as_view(), name="main-create"),
    path("main/<int:pk>/", MainDetailView.as_view(), name="main-detail"),
    path("main/<int:pk>/update", MainUpdateView.as_view(), name="main-update"),
    path("main/<int:pk>/delete", MainDeleteView.as_view(), name="main-delete"),

    path("project/", ProjectListView.as_view(), name="project-list"),
    path("project-create/", ProjectCreateView.as_view(), name="project-create"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("project/<int:pk>/update", ProjectUpdateView.as_view(), name="project-update"),
    path("project/<int:pk>/delete", ProjectDeleteView.as_view(), name="project-delete"),

    path("wage/", WageListView.as_view(), name="wage-list"),
    path("wage-create/", WageCreateView.as_view(), name="wage-create"),
    path("wage/<int:pk>/", WageDetailView.as_view(), name="wage-detail"),
    path("wage/<int:pk>/update", WageUpdateView.as_view(), name="wage-update"),
    path("wage/<int:pk>/delete", WageDeleteView.as_view(), name="wage-delete"),

    path("bonus/", BonusListView.as_view(), name="bonus-list"),
    path("bonus-create/", BonusCreateView.as_view(), name="bonus-create"),
    path("bonus/<int:pk>/", BonusDetailView.as_view(), name="bonus-detail"),
    path("bonus/<int:pk>/update", BonusUpdateView.as_view(), name="bonus-update"),
    path("bonus/<int:pk>/delete", BonusDeleteView.as_view(), name="bonus-delete"),
]

app_name = "salary"
