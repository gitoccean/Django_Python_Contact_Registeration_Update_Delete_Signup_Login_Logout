from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from project.forms import SignupForm,SigninForm,RegisterForm,DataForm
from django.contrib import messages
from project.models import SignupModel,RegisterModel,SigninModel
# Create your views here.


def HomePage(request):
   form = RegisterForm()
   register = RegisterModel.objects.all()


   return render(request, 'home.html', {'form': form, 'register': register})








def Signupview(request):
      form = SignupForm()

      if request.method == "POST":
          form = SignupForm(request.POST)

          if form.is_valid():
             form.save()
          else: 
             return render(request,'signup.html',{ 'form' : form})       
            
          return redirect('login') 
     
      return render(request,'signup.html',{ 'form' : form})




def SignUp_save(request):
  
    return render(request,'login.html')





def LoginPage(request):
    form = SigninForm()
    
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
         data = form.cleaned_data
         user=SignupModel.objects.filter(Username=data.get('Username')).first()
         if user is None:
           form.add_error('Username', " User do not exists!")
           return render(request,'login.html',{'form' : form})
         elif data.get('Password') != user.Password:
            form.add_error('Password', "passwords do not match !")
            return render(request,'login.html',{'form' : form})    
        
         return redirect('home')
    return render(request,'login.html',{'form' : form})



def LogoutPage(request):
    return render(request,'logout.html')



def RegisterPage(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
           form.save()
           return redirect('home')
    
    contex = { 'form' : form }
    return render(request,"register.html",contex) 
    



def Register_edit(request, id):
     
     register = RegisterModel.objects.get(id=id)
     form = RegisterForm(instance=register)

     if request.method == "POST":
         form = RegisterForm(request.POST,instance= register)
         if form.is_valid():
            form.save()
            return redirect('home')
         
     context = { 'form' : form }    
     return   render(request,'update.html',context)
        

   

def deleteID(request,id):
     register = RegisterModel.objects.get(id=id)
     if request.method == "POST":
         
         register.delete()
         return redirect("home")
     context= {'register':register}
     return render(request,'delete.html',context)

     