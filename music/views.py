from django.shortcuts import render
from django.http import HttpResponse            #http response sends back html/basic webpage
from django.conf.urls import include
from django.template import loader
from .models import Album

# Create your views here.
'''def index(request):
    all_objects = Album.objects.all()
    html = ''
    for album in all_objects:
        url = "/music/" + str(album.id) + "/"
        html += '<a href = "' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)
'''
def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)
    #return HttpResponse(template.render(context, request))

def detail(request, album_id):
    return HttpResponse("<h2>Details of Album with id:" + str(album_id)+ "</h2>")