from django.urls import path
from . import views

urlpatterns = [
    path('com_new/', views.com_new, name ='com_new'),
    path('community/<int:post_id>',views.community, name='community'),
    path('scrap/<int:post_id>',views.scrap, name='scrap'),
    path('com_update/<int:post_id>',views.com_update, name='com_update'),
    path('com_delete/<int:post_id>',views.com_delete,name='com_delete'),
    path('comList/', views.comList, name='comList'),

]