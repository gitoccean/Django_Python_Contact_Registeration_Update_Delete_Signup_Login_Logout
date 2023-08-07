from django.contrib import admin
from project.models import SignupModel,SigninModel,RegisterModel
# Register your models here.

class SignupAdmin(admin.ModelAdmin):
    list_display= ['Name','Email','Username','Password','Confirm_Password']

class SigninAdmin(admin.ModelAdmin):
    list_display= ['Username','Password']    

class RegisterAdmin(admin.ModelAdmin):
    list_display= ['id','name','email','phone','city','province','country']

admin.site.register(SignupModel,SignupAdmin)
admin.site.register(SigninModel,SigninAdmin)
admin.site.register(RegisterModel,RegisterAdmin)