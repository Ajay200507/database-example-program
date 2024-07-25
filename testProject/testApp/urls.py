from django.urls import path
import testApp.views as views

urlpatterns = [
    path('index',views.index,name='index'),
    path('html',views.index_html,name='index_html'),
    path('inserted',views.insert_data,name='inserted')

]