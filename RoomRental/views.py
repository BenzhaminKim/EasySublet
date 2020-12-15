from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Room
from .forms import RoomForm
# Create your views here.

def home_view(request,*args,**kwargs):
    '''
    Home Page View
    '''
    return render(request,'RoomRental/Home_Page.html')

def room_list_view(request, *args, **kwargs):
    '''
    Room List Page View
    '''

    rooms = Room.objects.all()
    context = {'rooms':rooms}

    return render(request,'RoomRental/RoomList_Page.html',context,status=200)

def room_detail_view(request,room_id,*args,**kwargs):
    '''
    Room Detail Page View
    '''

    room = get_object_or_404(Room, pk = room_id)
    context = {'room': room}

    return render(request,'RoomRental/RoomDetail_Page.html',context,status=200)

@login_required
def room_create_view(request,*args,**kwargs):
    '''
    Room Create Page View
    '''
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            room = Room.objects.create(title=title, content=content)
            room.user = request.user
            room.save()
            return redirect('room_list_view')
    else:
            
        form = RoomForm()
        context = {'page':'Create Room page','form' : form}
    return render(request,'RoomRental/RoomCreate_Page.html',context,status=200)


@login_required
def room_update_view(request,room_id,*args,**kwargs):
    '''
    Room Update Page View
    '''
    room = get_object_or_404(Room, pk = room_id)
    if request.user == room.user:
        form = RoomForm(request.POST or None, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list_view')
        context = {'page':'Update Room page','form' : form}
        return render(request,'RoomRental/RoomCreate_Page.html',context,status=200)
    else:
        return redirect('room_list_view')

@login_required
def room_delete_view(request,room_id,*args,**kwargs):
    '''
    Room Delete Page View
    '''
    room = get_object_or_404(Room,pk=room_id)
    if request.user == room.user:
        if request.method == 'POST':
            room.delete()
            return redirect('room_list_view')
        
        context = {'page':'Delete Room Page','room': room}
        return render(request,'RoomRental/RoomDelete_Page.html',context,status=200)
    else:
        return redirect('room_list_view')



