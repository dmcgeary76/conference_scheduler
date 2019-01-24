from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Session_Model, Choice_Model
from .forms import Session_Form, Choice_Form

# Custom view to list all sessions - mainly for testing
@login_required
def list_all_view(request, ts=0):
    # update the number of seats for each sessions
    seshs = Session_Model.objects.all()
    for sesh in seshs:
        sesh.seats = Choice_Model.objects.filter(session_id=sesh.id).count()
        sesh.save()
    session_times = {
        '1015': {'title': '', 'room': '', 'session_id': 0},
        '1130': {'title': '', 'room': '', 'session_id': 0},
        '1245': {'title': '', 'room': '', 'session_id': 0},
        '200':  {'title': '', 'room': '', 'session_id': 0}
    }
    times = ['10:15', '11:30', '12:45', '2:00']
    if ts == 0:
        try:
            all_sesh = Session_Model.objects.all().filter(time_slot=request.session['last_view']).order_by('title')
        except:
            all_sesh = Session_Model.objects.all().order_by('title')
    elif ts=='0:00':
        all_sesh = Session_Model.objects.all().order_by('title')
        request.session['last_view'] = 0
    else:
        all_sesh = Session_Model.objects.all().filter(time_slot=ts).order_by('title')
        request.session['last_view'] = ts
    for time_val in times:
        try:
            choi = get_object_or_404(Choice_Model, time_slot=time_val, user_id = request.user.id)
            sesh = get_object_or_404(Session_Model, id=choi.session_id)
            session_times[time_val.replace(':','')]['title'] = sesh.title
            session_times[time_val.replace(':','')]['room'] = sesh.room
            session_times[time_val.replace(':','')]['session_id'] = sesh.id
        except:
            pass
    print(session_times)
    context = {
        'all_sesh': all_sesh,
        'session_times': session_times,
    }
    return render(request, 'list_all.html', context)


@login_required
def delete_choice_view(request, pk):
    sesh = get_object_or_404(Choice_Model, session_id=pk, user_id = request.user.id)
    sesh.delete()
    return HttpResponseRedirect(reverse('list_all_view'))


# Show the details of an individual session
@login_required
def details_view(request, pk=0):
    current_user = request.user
    if pk == 0:
        pk = request.session['sesh_id']
    else:
        request.session['sesh_id'] = pk
    sesh = Session_Model.objects.get(id=pk)
    print(sesh.id)
    try:
        registrants = Choice_Model.objects.all().filter(session_id=sesh.id)
        attendees = []
        for registrant in registrants:
            user = User.objects.get(id = registrant.user_id)
            attendees.append({
                'first_name':   user.first_name,
                'last_name':    user.last_name,
                'email':        user.email})
    except:
        attendees = {}
        pass
    is_owner = request.user.username == sesh.email
    print(is_owner)
    try:
        this_time = get_object_or_404(Choice_Model, time_slot=sesh.time_slot, user_id = current_user.id)
        has_choice = True
        if this_time.session_id == sesh.id:
            same_sesh = True
        else:
            same_sesh = False
    except:
        has_choice = False
        same_sesh = False
    form = Choice_Form(request.POST or None)
    if form.is_valid():
        if has_choice:
            this_time.delete()
        form.save()
        return HttpResponseRedirect(reverse('list_all_view'))
    else:
        context = {
            'sesh': sesh,
            'has_choice': has_choice,
            'same_sesh': same_sesh,
            'is_owner': is_owner,
            'attendees': attendees
        }
        return render(request, 'details.html', context)


# Junk view assignment until I can replace it with a proper menu
@login_required
def home_view(request):
    return render(request, "home.html", {})


@login_required
def create_session_view(request):
    form = Session_Form(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list_all_view'))
    else:
        context = {
            'form': form
        }
    return render(request, 'create_session.html', context)
