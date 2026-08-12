from django.views.generic import TemplateView

# Create your views here.
# Function Based Views vs. Class Based Views
#

class HomePageView(TemplateView):
  template_name = "pages/home.html"

class AboutPageView(TemplateView):
  template_name = "pages/about.html"