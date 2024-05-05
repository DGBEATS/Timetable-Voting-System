from django.contrib import admin


from .models import Room, RoomActivity, Message  # add the Room models into the admin page (User model is registered by default)

admin.site.register(Room)
admin.site.register(RoomActivity)
admin.site.register(Message)