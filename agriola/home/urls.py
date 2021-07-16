from os import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import uploadImage,ImageDisplay
#from .views import FileFieldFormView
urlpatterns = [
    
    #path('',views.index,name='index'),
    
    path('',views.home2,name='home2'),
    path('about',views.about,name='about'),
    path('pricing',views.pricing,name='pricing'),
    path('features',views.features,name='features'),
    path('Try_detect_Change',views.Try_detect_Change,name='Try_detect_Change'),
    #path('Try_detect_Change1',views.Try_detect_Change1,name='Try_detect_Change1'),
    path('demo',views.demo,name='demo'),
    #path('test',uploadimage.as_view(),name='test'),
    #path('test2',ImageDisplay.as_view(),name='test2'),
    path('test3',views.test3,name='test3')
    #path('test3', FileFieldFormView.as_view(), name='test3')
    

    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)