from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Meep

#Unregister group
admin.site.unregister(Group)

#mix profile info into user info
class ProfileInline(admin.StackedInline):
	model = Profile

#Extend our user model
class UserAdmin(admin.ModelAdmin):
	model= User
	# Just display Username Field on Admin page
	fields = ["username"]
	inlines = [ProfileInline]

#unregister initial user
admin.site.unregister(User)
#Reregister User with UserAdmin class and Profile
admin.site.register(User, UserAdmin)	
admin.site.register(Profile)

#register meep
admin.site.register(Meep)

