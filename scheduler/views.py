from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .models import Event, Session, Speaker
from .forms import EventForm, SessionForm, SpeakerForm
from django.utils import timezone
from datetime import datetime, date

def home(request):
    events = Event.objects.all().order_by('start_date')
    context = {
        'events': events,
    }
    return render(request, 'scheduler/home.html', context)

@login_required
def events(request):
    events = Event.objects.all().order_by('-created_at')
    context = {
        'events': events,
    }
    return render(request, 'scheduler/events.html', context)

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('home')
    else:
        form = EventForm()
    
    context = {
        'form': form,
        'title': 'Create New Event'
    }
    return render(request, 'scheduler/event_form.html', context)

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('home')
    else:
        form = EventForm(instance=event)
    
    context = {
        'form': form,
        'title': 'Edit Event'
    }
    return render(request, 'scheduler/event_form.html', context)

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('home')
    
    context = {
        'event': event
    }
    return render(request, 'scheduler/event_confirm_delete.html', context)

@login_required
def view_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    sessions = event.sessions.all().order_by('start_time')
    
    # Get all speakers for this event's sessions
    speakers = Speaker.objects.filter(session__event=event).distinct()
    
    context = {
        'event': event,
        'sessions': sessions,
        'speakers': speakers,
    }
    return render(request, 'scheduler/event_detail.html', context)

@login_required
def sessions(request):
    sessions = Session.objects.all().order_by('-start_time')
    return render(request, 'scheduler/sessions.html', {'sessions': sessions})

@login_required
def create_session(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Session created successfully!')
                return redirect('sessions')
            except ValidationError as e:
                messages.error(request, str(e))
    else:
        form = SessionForm()
        # Pre-select event if provided in URL
        event_id = request.GET.get('event')
        if event_id:
            form.fields['event'].initial = event_id
    return render(request, 'scheduler/session_form.html', {'form': form, 'title': 'Create Session'})

@login_required
def speakers(request):
    speakers = Speaker.objects.all().order_by('name')
    return render(request, 'scheduler/speakers.html', {'speakers': speakers})

@login_required
def create_speaker(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Speaker created successfully!')
            return redirect('speakers')
    else:
        form = SpeakerForm()
    
    context = {
        'form': form,
        'title': 'Create New Speaker'
    }
    return render(request, 'scheduler/speaker_form.html', context)

@login_required
def delete_speaker(request, speaker_id):
    speaker = get_object_or_404(Speaker, id=speaker_id)
    if request.method == 'POST':
        speaker.delete()
        messages.success(request, 'Speaker deleted successfully!')
        return redirect('speakers')
    return render(request, 'scheduler/speaker_confirm_delete.html', {'speaker': speaker})

@login_required
def edit_session(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Session updated successfully!')
                return redirect('sessions')
            except ValidationError as e:
                messages.error(request, str(e))
    else:
        form = SessionForm(instance=session)
    
    context = {
        'form': form,
        'title': 'Edit Session',
        'is_edit': True
    }
    return render(request, 'scheduler/session_form.html', context)

@login_required
def schedule(request):
    events = Event.objects.all().order_by('start_date')
    return render(request, 'scheduler/schedule.html', {'events': events})