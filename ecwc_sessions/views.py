from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Session_Model, Choice_Model, gSession_Model
from .forms import Session_Form, Choice_Form

# Custom view to list all sessions - mainly for testing
@login_required
def list_all_view(request, ts=0):
    # update the number of seats for each sessions
    seshs = Session_Model.objects.all()
    for sesh in seshs:
        sesh.seats = Choice_Model.objects.filter(session_id=sesh.id, time_slot=sesh.time_slot).count()
        sesh.save()
    session_times = {
        '1015': {'title': '', 'room': '', 'session_id': 0},
        '1130': {'title': '', 'room': '', 'session_id': 0},
        '1245': {'title': '', 'room': '', 'session_id': 0},
        '200':  {'title': '', 'room': '', 'session_id': 0}
    }
    times = ['10:15 A.M.', '11:30 A.M.', '12:45 P.M.', '2:00 P.M.']
    if ts == 0:
        if request.session['last_view']:
            pass
        else:
            request.session['last_view'] = '0:00'
        try:
            all_sesh = Session_Model.objects.all().filter(time_slot=request.session['last_view']).order_by('title')
        except:
            all_sesh = Session_Model.objects.all().order_by('title')
    elif ts=='0:00':
        all_sesh = Session_Model.objects.all().order_by('title')
        request.session['last_view'] = '0:00'
    else:
        all_sesh = Session_Model.objects.all().filter(time_slot=ts).order_by('title')
        request.session['last_view'] = ts
    for time_val in times:
        try:
            choi = get_object_or_404(Choice_Model, time_slot=time_val, user_id = request.user.id)
            sesh = get_object_or_404(Session_Model, id=choi.session_id)
            session_times[time_val.split(' ')[0].replace(':','')]['title']      = sesh.title
            session_times[time_val.split(' ')[0].replace(':','')]['room']       = sesh.room
            session_times[time_val.split(' ')[0].replace(':','')]['session_id'] = sesh.id
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
    try:
        seshs = Choice_Model.objects.filter(session_id=pk, user_id=request.user.id)
        seshs.delete()
    except:
        print('Something went wrong.')
    '''
    sesh = get_object_or_404(Session_Model, id=pk)
    choi = get_object_or_404(Choice_Model, session_id=pk, user_id = request.user.id, time_slot = sesh.time_slot)
    choi.delete()
    if sesh.duration == '2 Hours':
        choi2 = get_object_or_404(Choice_Model, session_id=pk, user_id = request.user.id)
    '''
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
        registrants = Choice_Model.objects.all().filter(session_id=sesh.id, time_slot=sesh.time_slot)
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
    is_owner = False
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
    temp_time = ''
    if sesh.duration == '2 Hours':
        if sesh.time_slot == '10:15 A.M.':
            temp_time = '11:30 A.M.'
        else:
            temp_time = '2:00 P.M.'
        try:
            this_time = get_object_or_404(Choice_Model, time_slot=temp_time, user_id = current_user.id)
            has_choice = True
        except:
            pass
    form = Choice_Form(request.POST or None)
    if form.is_valid():
        if has_choice:
            old_seshs = Choice_Model.objects.filter(session_id=this_time.session_id, user_id=request.user.id)
            old_seshs.delete()

        # If it is a 2 Hour Session, then book it for two time slots
        if sesh.duration == '2 Hours':
            ext_time = ''
            if sesh.time_slot == '10:15 A.M.':
                ext_time = '11:30 A.M.'
            elif sesh.time_slot == '11:30 A.M.':
                ext_time = '12:45 P.M.'
            else:
                ext_time = '2:00 P.M.'
            ext_choi = Choice_Model(
                session_id  = sesh.id,
                user_id     = current_user.id,
                time_slot   = ext_time
            )
            ext_choi.save()
        form.save()
        if 'Gold' in sesh.title:
            return HttpResponseRedirect(reverse('gdetails_view'))
        else:
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


@login_required
def gdetails_view(request, pk=0):
    print('hello')
    return HttpResponseRedirect(reverse('list_all_view'))


# Junk view assignment until I can replace it with a proper menu
@login_required
def home_view(request):
    return render(request, "home.html", {})


# Function to delete session instances
@login_required
def delete_session_view(request, pk):
    instance = get_object_or_404(Session_Model, id=pk)
    instance.delete()
    try:
        chois = Choice_Model.objects.filter(session_id=pk)
        chois.delete()
    except:
        pass
    return HttpResponseRedirect(reverse('list_all_view'))


# Search to capture a search string
@login_required
def searchit(request):
    if request.method == 'POST':
            form = Search_Form(request.POST) # if post method then form will be validated
            if form.is_valid():
                cd = form.cleaned_data
                num1 = cd.get('search_string')
                result = cd.get('result')
                if result:
                    all_sesh = Session_Model.objects.filter(title__contains=search_string)
                context = {
                    'all_sesh': all_sesh
                }
                return render(request, 'list_all.html', context)



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


@login_required
def edit_session_view(request, pk=0, template='edit_session.html'):
    current_user = request.user
    if pk == 0:
        pk = request.session['sesh_id']
    else:
        request.session['sesh_id'] = pk
    sesh = get_object_or_404(Session_Model, id=pk)
    form = Session_Form(request.POST or None, instance=sesh)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list_all_view'))
    else:
        print('not valid')
        context = {
            'form': form
        }
    return render(request, 'edit_session.html', context)
