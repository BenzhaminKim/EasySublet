from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Room, Image
from .forms import RoomForm, ImageForm
import logging
# Create your views here.

def home_view(request,*args,**kwargs):
    '''
    Home Page View
    '''
    logger = logging.getLogger("loggers")
    logger.info(request)
    return render(request,'Common/Home_Page.html')

def room_list_view(request, *args, **kwargs):
    '''
    Room List Page View
    '''
    logger = logging.getLogger("loggers")

    rooms = Room.objects.all()
    context = {'rooms':rooms}
    logger.info(context)
    return render(request,'RoomList_Page.html',context,status=200)
@login_required
def my_room_list_view(request, *args, **kwargs):
    '''
    Room List Page View
    '''

    logger = logging.getLogger("loggers")
    rooms = Room.objects.filter(user=request.user)
    room_with_images = []
    for room in rooms:
        images = Image.objects.filter(room=room).filter().first()
        room_with_images.append({
            'room':room,
            'images':images
        })
    context = {'room_with_images':room_with_images}
    logger.info(context)
    return render(request,'MyRoom_Page.html',context,status=200)


def room_detail_view(request,room_id,*args,**kwargs):
    '''
    Room Detail Page View
    '''
    logger = logging.getLogger("loggers")
    room = get_object_or_404(Room, pk = room_id)
    images = Image.objects.filter(room=room)
    
    context = {'room': room, 'images':images }
    logger.info(context)

    return render(request,'RoomDetail_Page.html',context,status=200)

def room_images_view(request,room_id,*args,**kwargs):
    '''
    Room Detail Page View
    '''
    logger = logging.getLogger("loggers")

    room = get_object_or_404(Room, pk = room_id)
    images = Image.objects.filter(room=room)
    context = {'images':images, 'room_id':room_id }
    logger.info(context)

    return render(request,'Room_Images_Page.html',context,status=200)

@login_required
def room_create_view(request,*args,**kwargs):
    '''
    Room Create Page View
    '''
    logger = logging.getLogger("loggers")
    if request.method == 'POST':
        room_form = RoomForm(request.POST)
        images = request.FILES.getlist('image')
        print(room_form.is_valid(), room_form.cleaned_data)
        if room_form.is_valid():
            room = room_form.save()
            room.user = request.user
            room.save()
            for image in images:
                Image.objects.create(room=room, image=image)
            logger.info(room)
            return redirect('room_detail_view',room_id=room.id)

    room_form = RoomForm()
    image_form = ImageForm()
    context = {'page':'Create Room page','room_form':room_form,'image_form':image_form}
    logger.info(context)
    return render(request,'RoomCreate_Page.html',context,status=200)


@login_required
def room_update_view(request,room_id,*args,**kwargs):
    '''
    Room Update Page View
    '''
    logger = logging.getLogger("loggers")
    room = get_object_or_404(Room, pk = room_id)
    if request.user == room.user:
        room_form = RoomForm(request.POST or None, instance=room)
        image_form = ImageForm()
        images = request.FILES.getlist('image')
        if room_form.is_valid():
            room_form.save()
            if len(images) > 0:
                prev_images = Image.objects.filter(room = room)
                prev_images.delete()
                for image in images:
                    Image.objects.create(room=room, image=image)
                    
            logger.info(room_form)
            return redirect('room_detail_view',room_id=room.id)
        context = {'page':'Update Room page','room_form' : room_form,'image_form':image_form}
        logger.info(context)
        return render(request,'RoomCreate_Page.html',context,status=200)
    else:
        logger.warning(request)
        return redirect('room_list_view')

@login_required
def room_delete_view(request,room_id,*args,**kwargs):
    '''
    Room Delete Page View
    '''
    logger = logging.getLogger("loggers")
    room = get_object_or_404(Room,pk=room_id)
    if request.user == room.user:
        if request.method == 'POST':
            room.delete()
            logger.info(room)
            return redirect('room_list_view')
        
        context = {'page':'Delete Room Page','room': room}
        logger.info(context)
        return render(request,'RoomDelete_Page.html',context,status=200)
    else:
        logger.info(request)
        return redirect('room_list_view')



