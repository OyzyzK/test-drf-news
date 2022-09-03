from django.template.context_processors import static
from django.urls import path

from createnews import views
from django.conf.urls.static import static

from createnews.views import NewListJson, NewIDJson
from news import settings

urlpatterns = [
    path('news_h/', views.index),
    path('news_h/<int:pk>/', views.news_id),
    path('news/', NewListJson.as_view()),
    path('news/<int:pk>',NewIDJson.as_view())
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
