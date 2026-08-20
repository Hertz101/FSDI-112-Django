from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView
)
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView): # GET Request -> List
    # template_name attribute renders specfic html file
    template_name = "posts/list.html"
    #model attribute let django know from which model (table we want to retrieve the data
    model = Post
    # context_object_name attribute allow us to change the name on how we call it inside of the templates
    context_object_name = "posts"

    # SELECT * FROM posts

class PostDetailView(DetailView): # Get Request -> Single Object
  template_name = "posts/detail.html"
  model = Post
  context_object_name = "single_post"

  # SELECT * FROM posts WHERE id = ?

class PostCreateView(CreateView): # POST Request -> New Object / Empty form (HTML)
  template_name = "posts/new.html"
  model = Post
  # fields attributes is a list that allows us to enable/disable the inputs to render in the form
  fields = ["title", "subtitle", "body"]

  def form_valid(self, form):
    # This function help us to run some validations before we create the object
    form.instance.author = User.objects.last() #admin/last user
    return super().form_valid(form)

class PostUpdateView(UpdateView): # POST Request -> A for to update an existing object
  template_name = "posts/edit.html"
  model = Post
  fields = ["title", "subtitle", "body"]

class PostDeleteView(DeleteView): #Post request -> A form to handle the delete functionallity
  template_name = "posts/delete.html"
  model = Post
  # success_url attribute allow us to redirect the user to another view if the request is successful
  success_url = reverse_lazy("post_list")