from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Video, New, Podcast
from .services import open_file, open_audio_file
import os


def get_list_video(request):
    return render(request, 'video_hosting/home.html', {'video_list': Video.objects.all()})


def get_video(request, pk: int):
    _video = get_object_or_404(Video, id=pk)
    return render(request, "video_hosting/video.html", {"video": _video})


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')
    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

def get_streaming_audio(request, pk: int):
    file, status_code, content_length, content_range = open_audio_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')
    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

def get_list_podcasts(request):
    return render(request, 'video_hosting/podcasts.html', {'podcasts': Podcast.objects.all()})

def get_detail_podcast(request, pk: int):
    podcast = get_object_or_404(Podcast, id=pk)
    context = {
        'podcast': podcast
    }
    return render(request, 'video_hosting/podcastDetail.html', context)

def get_news_list(request):
    return render(request, 'video_hosting/news.html', {'News_list': New.objects.all()})

def get_news_detailList(request, pk: int):
    news = get_object_or_404(New, id=pk)
    context = {
        'news': news
    }
    return render(request, 'video_hosting/newsDetail.html', context)




