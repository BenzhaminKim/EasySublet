from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Room, Image
from .forms import RoomForm, ImageForm
# Create your views here.

def home_view(request,*args,**kwargs):
    '''
    Home Page View
    '''
    return render(request,'Common/Home_Page.html')

def room_list_view(request, *args, **kwargs):
    '''
    Room List Page View
    '''

    rooms = Room.objects.all()
    context = {'rooms':rooms}

    return render(request,'RoomList_Page.html',context,status=200)

def room_detail_view(request,room_id,*args,**kwargs):
    '''
    Room Detail Page View
    '''

    room = get_object_or_404(Room, pk = room_id)
    images = Image.objects.filter(room=room)
    context = {'room': room, 'images':images}

    return render(request,'RoomDetail_Page.html',context,status=200)

@login_required
def room_create_view(request,*args,**kwargs):
    '''
    Room Create Page View
    '''
    if request.method == 'POST':
        room_form = RoomForm(request.POST)
        images = request.FILES.getlist('image')
        print(images)
        if room_form.is_valid():
            title = room_form.cleaned_data['title']
            description = room_form.cleaned_data['description']
            room = Room.objects.create(title=title, description=description)
            room.user = request.user
            room.save()
            for image in images:
                Image.objects.create(room=room, image=image)
            return redirect('room_list_view')

    room_form = RoomForm()
    image_form = ImageForm()
    context = {'page':'Create Room page','room_form':room_form,'image_form':image_form}
    return render(request,'RoomCreate_Page.html',context,status=200)


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
        return render(request,'RoomCreate_Page.html',context,status=200)
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
        return render(request,'RoomDelete_Page.html',context,status=200)
    else:
        return redirect('room_list_view')



