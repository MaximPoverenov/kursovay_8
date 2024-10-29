from django.urls import path
from .views import HabitListCreateView, HabitDetailView, PublicHabitListView

app_name = "habits"

urlpatterns = [
    # Маршрут для списка привычек и создания новой
    path("habits/", HabitListCreateView.as_view(), name="habit-list-create"),
    # Маршрут для просмотра, обновления или удаления конкретной привычки
    path("habits/<int:pk>/", HabitDetailView.as_view(), name="habit-detail"),
    path("public-habits/", PublicHabitListView.as_view(), name="public-habit-list"),
]