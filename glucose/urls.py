from django.urls import path
from .views import Levels, LevelsByUser,CreateLevel

urlpatterns = [
    path('', Levels.as_view(), name='levels-view'),
    path('<int:id>/', LevelsByUser.as_view(), name='levels-view-by-user'),
    path('create/', CreateLevel.as_view(), name='levels-create'),
]
