from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render

# Create your views here.
# Function Based Views vs. Class Based Views
  
# Class Based Views
class HomePageView(TemplateView): #Heritage - OOP. (Object Oriented Programming)
  template_name = "pages/home.html"

  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    context["name"] = "Adam"
    return context


class AboutPageView(TemplateView):
  template_name = "pages/about.html"

# Function Based Views
def contact_page(request):
  # return HttpResponse("Hello World from a FBV")
  
  contact_info = {
    "name": "Adam",
    "address": "somewhere in colorado",
    "email": "adamdog@gmail.com"
  }

  return render(request, "pages/contact.html", contact_info)