from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, RoomActivity, Message
from .forms import RoomForm


# Create your views here. 'Views' is the request handler page

def loginPage(request):
    page = 'login_registration'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')  # get username and password

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist.")  # check if the user exists

        user = authenticate(request, username=username,
                            password=password)  # makes sure the login in details are correct

        if user is not None:
            login(request, user)
            return redirect('home')  # login the user and redirect them
        else:
            messages.error(request, "Username or password does not exist")

    context = {'page': page}
    return render(request, 'base/login_registration.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm() # uses Django's in build form for making a user

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error has occured during registration')

    return render(request, 'base/login_registration.html', {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(roomActivity__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    # collects all the rooms in my database
    # querying the database and collecting all the room information from it instead of our generation of data

    roomActivitys = RoomActivity.objects.all()  # collects all the activities in room activity Note - Consider filtering higher priority
    # room activities for the purpose of voting
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__roomActivity__name__icontains=q))

    context = {'rooms': rooms, 'roomActivitys': roomActivitys, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/Home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    roomMessages = room.message_set.all() #.order_by('-created')  give the all the sets of messages related to this room (most recent messge first)
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')

        )
        room.participants.add(request.user) # add a participant then render their information out
        return redirect('room', pk=room.id)

    context = {'room': room, 'roomMessages': roomMessages, 'participants': participants}
    return render(request, 'base/Room.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all() # get all children of a specific object
    room_messages = user.message_set.all()
    roomActivitys = RoomActivity.objects.all()

    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages, 'roomActivitys': roomActivitys}
    return render(request, 'base/Profile.html', context)


@login_required(login_url="login_registration")
def createRoom(request):  # CRUD CREATE(POST) REQUEST TO CREATE A NEW ROOM
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)  # <- adds a new room using POST
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user # Adds a host based on who is logged in
            room.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login_registration')
def updateRoom(request, pk):  # CRUD Update REQUEST TO update A existing ROOM
    room = Room.objects.get(id=pk)  # get the room by its id
    form = RoomForm(instance=room)  # create a form with the existing data of a room

    if request.user != room.host:
        return HttpResponse(
            'You are not allowed to access this port')  # if you are not the room user, you cannot access updating this room

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)  # <- setting the instance to be updated to be the room that I
        # just pulled from the database
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login_registration')
def deleteRoom(request, pk):  # send the user to a delete page (not a delete form like update)
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not allowed to access this port')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/Delete.html', {'obj': room})

@login_required(login_url='login_registration')
def deleteMessage(request, pk):  # send the user to a delete page (not a delete form like update)
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse('You are not the associated user to this message!')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/Delete.html', {'obj': message})
