from django.urls import path

from . import views

app_name = 'people'
urlpatterns = [
          # Home page
          path('',views.index,name='index'),
          # Page that shows all the topic
          path('topic/<int:topic_id>/',views.topic,name='topic'),
          path('topics',views.topics,name='topics'),
          path('new_topic/',views.new_topic,name='new_topic'),
          path('new_entry/<int:topic_id>',views.new_entry,name='new_entry'),
        ]
