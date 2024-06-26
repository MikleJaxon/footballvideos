from django.urls import path
from video_hosting.views import get_list_video, get_video, get_list_podcasts, get_news_list, get_news_detailList, get_streaming_video, get_detail_podcast, get_streaming_audio

app_name = 'video_hosting'

urlpatterns = [
    path('stream/<int:pk>/', get_streaming_video, name='stream'),
    path('<int:pk>/', get_video, name='video'),
    path('', get_list_video, name='home'),
    path('news/', get_news_list, name='news'),
    path('news/<int:pk>/', get_news_detailList, name='news_detail'),
    path('podcasts/', get_list_podcasts, name='podcasts'),
    path('podcasts/<int:pk>/', get_detail_podcast, name='podcast_detail'),
    path('audio/<int:pk>/', get_streaming_audio, name='podcast_audio'),
   

]
