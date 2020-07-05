from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
    path('home/', views.UploadFormView.as_view(), name='home'),
    path('results/<label>', views.ResultView, name='results'),
]