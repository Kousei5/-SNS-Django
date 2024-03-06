from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some':100})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています。'})
    return render(request, 'signup.html')

def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            render(request, 'login.html', {})
    return render(request, 'login.html', {})

#@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'detail.html', {'object':object, 'user': request.user})

def goodfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    object.good = object.good + 1
    object.save()
    return redirect('list')

def readfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('list')
    else:
        object.read = object.read + 1
        object.readtext = object.readtext + ' ' + username #同じ名前だと区別できない
        object.save()
        return redirect('list')

class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel 
    fields = ('title', 'content', 'author', 'snsimage')
    success_url = reverse_lazy('list')

class UpdatePost(UpdateView,UserPassesTestMixin):
    model = BoardModel
    template_name = 'update.html'
    fields = ('title', 'content', 'author', 'snsimage')

    def get_success_url(self,  **kwargs):
        pk = self.kwargs["pk"]
        return reverse_lazy('detail', kwargs={"pk": pk})
   
    def test_func(self, **kwargs):
        pk = self.kwargs["pk"]
        object = BoardModel.objects.get(pk=pk)
        return (object.author == self.request.user) 

class DeletePost( DeleteView):
    model = BoardModel
    template_name = 'delete.html'
    success_url = reverse_lazy('list')

    