"""learning_logs URL Configuration"""

from django.urls import path

from learning_logs import views

app_name = 'learning_logs'
urlpatterns = [  #  схемы URL
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Page with detailed information on a specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Add new topic page
    path('new_topic/', views.new_topic, name='new_topic'),
    # Add new entry page
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Edit entry page
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
