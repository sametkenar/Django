#from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Merhaba Django!")

# home/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content','published']
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','content','published']
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
