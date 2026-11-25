from django.shortcuts import render
from .models import  Topic, Entry
# Create your views here.


def index(request):
    return render(request,'people/index.html')


def topics(request):
    """ Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics' : topics}
    return render (request,'people/topics.html',context)


def topic(request,topic_id):
    """Show individual topic fr all its entries"""
    topics = Topic.objects.get(id=topic_id)
    entries = topics.entry_set.order_by('-date_added')
    context = {'topics': topics, 'entries': entries}
    return render (request,'people/topic.html',context)
