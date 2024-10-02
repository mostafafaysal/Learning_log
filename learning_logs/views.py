from django.shortcuts import render,redirect,get_object_or_404
from .models import Topic,Entry
from .forms import TopicForm,EntryForm

from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    """The home page for learning log """
    return render(request,"learning_logs/index.html")

@login_required
def topics(request):
    """Topics list page"""
    topics=Topic.objects.filter(owner= request.user).order_by('date_added')
    context= {'topics':topics}
    return render(request,"learning_logs/topics.html",context)

@login_required
def topic(request,topic_id):
    """topic entry """
    # topic= Topic.objects.get(id=topic_id)
    topic= get_object_or_404(Topic,id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entrys = topic.entry_set.order_by("-date_added")
    context = {"topic":topic,"entrys":entrys}
    return render(request,"learning_logs/topic.html",context)

@login_required
def new_topic(request):
    """Add new topic."""
    if request.method != "POST":
        #No data submitted create a new form
        form = TopicForm()
    else:
        #post data submitted: process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.owner= request.user
            new_form.save()
            return redirect('learning_logs:topics')
    #display blank or invalid form
    context = {'form':form}
    return render(request,"learning_logs/new_topic.html",context)

@login_required
def new_entry(request,topic_id):
    """Add new entry """
    topic= Topic.objects.get(id=topic_id)
    if request.method !="POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic',topic_id=topic_id)
    context= {'topic':topic,"form":form}
    return render(request,"learning_logs/new_entry.html",context)

@login_required
def edit_entry(request,entry_id):
    """edit entry"""
    entry=Entry.objects.get(id = entry_id)
    topic = entry.topic

    if topic.owner !=request.user:
        raise Http404

    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id= topic.id)
    context = {'entry':entry,'topic':topic,"form":form}
    return render(request,"learning_logs/edit_entry.html",context)
