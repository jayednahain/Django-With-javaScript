
from django.contrib import admin
from django.urls import path
from spinner_js import views
from spinner_js.views import PostTemplateView,json_data_response,CreatePost

urlpatterns = [

    path('',views.home_view,name='home_view_link'),
    path('spinnerdata/',PostTemplateView.as_view(),name='spinner_view'),
    path('json_response/',json_data_response,name="json_response_link"),
    path('test_js/',views.test_js,name ='test_js_link'),

    path('create_post/',CreatePost.as_view(),name ='create_post')

]
