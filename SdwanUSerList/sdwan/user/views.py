# -*- coding: utf-8 -*-


from django.shortcuts import render, redirect
from user.forms import UserForm
from user.models import User

# Create your views here.

def user1(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = UserForm()
    return render(request,'index.html',{'form':form})
    
    
def show(request):
    user_list = User.objects.all()
    return render (request,'show.html',{'user_list':user_list})


def edit(request,id):
    user_list = User.objects.get(id=id)
    form = UserForm(request.POST,instance = user_list)
    return render(request,'edit.html',{'user_list':user_list})


def update(request,id):
    user_list = User.object.get(id=id)
    form = UserForm(request.POST,instance = user_list)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'user_list':user_list})



def destroy(request,id):
    user_list = User.objects.get(id=id)
    user_list.delete()
    return redirect('/show')




# def index(request):
#     return render(request, 'vyos/index1.html')

# def User1(request):
#     user_list = User.objects.order_by('-date')
#     return user_list