from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Song

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})

def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'songs/song_detail.html', {'song': song})

def song_lyrics(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return JsonResponse({"title": song.title, "lyrics": song.lyrics})
