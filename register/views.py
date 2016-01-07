from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from register.models import *



def Home(request):
    Header = "Welcome To My Students Portal"
    if request.method == "GET":
        form = StudentForm();
        
        return render(request,'register/Homepage.html',{'form':form,'Header':Header})
    elif request.method == "POST":
        form = StudentForm(request.POST)
        
        form.save()
        
        return HttpResponseRedirect('/register/commentform/')
    #return render(request,'register/Homepage.html',{'Header':Header},{'form':form})

def Regista(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/regista_success/') 
        
    args = {}
    args.update(csrf(request))
    #cross site refory
    args['form'] = UserCreationForm()

    return render_to_response('register/register.html',args)
def register_success(request):
    return render_to_response('register/register_sucess.html')


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('register/login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('register/loggedin')
    else:
        return HttpResponseRedirect('register/invalid') 

def loggedin(request):
    return render_to_response('register/loggedin.html',{'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('register/logout.html')


def StudentList(request):
    students = StudentName.all();
    return render_to_response('register/all_students.html',{'students':students})


##def StudentEntryForm(request):
##    if request.method == "GET":
##        form = StudentForm();
##        return render(request,'register/Homepage.html',{'form':form})
##    elif request.method == "POST":
##        form = StudentForm(request.POST)
##        form.save()
##        return HttpReponseRedirect('/register')
        
def CommentEntryForm(request):
    H1 = "Welcome To My Student Comment Portal"
    H2 = "Comment Here If Your a Registered Student"
    s = StudentName.objects.get(id=1)
    c = s.comment_set.all()
    
    if request.method == "GET":
        form = CommentForm()
        return render(request,'register/commententryform.html',{'form':form,'H1':H1,'H2':H2,'c':c})
    elif request.method == "POST":
        form = CommentForm(request.POST)
        form.save()
        return HttpResponseRedirect('/register/commentform/')

     
    
