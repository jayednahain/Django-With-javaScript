from django.shortcuts import render

from django.views.generic import TemplateView,CreateView
from Ex_Data.models import Post
from django.http import JsonResponse

# Create your views here.

class PostTemplateView(TemplateView):
   #the template view will empty !
   #so we use the response from json_data_response() and show it to template view
   template_name = 'spinner_js/template_view.html'

class CreatePost(CreateView):
   model = Post
   template_name ='spinner_js/create_post.html'
   fields = '__all__'


def json_data_response(request):
   #inseted of all we are using values !
   all_data = list(Post.objects.values())

   return JsonResponse(all_data,safe=False)








def home_view(request):
   return render(request,'spinner_js/home.html')

def SpinnerView(request):
   return render(request, 'spinner_js/spinner.html')

def test_js(request):
   return render(request,'spinner_js/test_js.html')