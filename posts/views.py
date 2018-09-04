from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import News

def home(request):
	news = News.objects.all()
	return render(request, 'home.html', {'news':news})

@login_required
def news(request, pk):
	news = get_object_or_404(News, pk=pk)
	return render(request, 'news.html', {'news': news})
