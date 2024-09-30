"""define URL patterns for learning log"""
from django.urls import path
from . import views


app_name = "learning_logs"

urlpatterns= [
    #homepage
    path("",views.index, name="index"),
    #All topics list
    path("topics/", views.topics, name="topics"),
    # single topic page
    path("topics/<int:topic_id>",views.topic, name="topic"),
    # Add new topic
    path("new_topic/",views.new_topic, name="new_topic"),
    # Add entry to a topic
    path("new_entry/<int:topic_id>", views.new_entry, name="new_entry"),
    # edit entry
    path("edit_entry/<int:entry_id>",views.edit_entry,name="edit_entry"),

]