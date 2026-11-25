from django.urls import path

from . import views

app_name = 'people'
urlpatterns = [
          # Home page
          path('',views.index,name='index'),
          # Page that shows all the topic
          path('topic/<int:topic_id>/',views.topic,name='topic'),
          path('topics',views.topics,name='topics'),
        ]
