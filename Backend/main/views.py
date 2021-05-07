from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, PostForms, EditForms
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from .models import Post


def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)

            return redirect('login')
    context = {'form': form}
    return render(request, 'Accounts/register.html', context)


def loginPage(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Post_list')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'Accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
class homepage(ListView):
    model = Post
    template_name = 'Accounts/Post_list.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = "Accounts/article_detail.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForms
    template_name = "Accounts/add_post.html"
    #fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForms
    template_name = "Accounts/update_post.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "Accounts/delete_post.html"
    success_url = reverse_lazy('Post_list')
