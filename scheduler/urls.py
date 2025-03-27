from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import auth as auth_views_custom

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', auth_views.LoginView.as_view(template_name='scheduler/login.html', next_page='events'), name='default'),
    path('events/', views.events, name='events'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:event_id>/', views.view_event, name='view_event'),
    path('events/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('events/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('sessions/', views.sessions, name='sessions'),
    path('sessions/create/', views.create_session, name='create_session'),
    path('speakers/', views.speakers, name='speakers'),
    path('speakers/create/', views.create_speaker, name='create_speaker'),
    path('speakers/<int:speaker_id>/delete/', views.delete_speaker, name='delete_speaker'),
    path('schedule/', views.schedule, name='schedule'),
    path('login/', auth_views.LoginView.as_view(template_name='scheduler/login.html', next_page='events'), name='login'),
    path('register/', auth_views_custom.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login', template_name=None), name='logout'),
]