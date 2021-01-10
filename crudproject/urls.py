from django.contrib import admin
from django.urls import path,include
import crud.views
import kakaopay.views
import accounts.views
import community.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud.views.main, name='main'),
    path('crud/<int:post_id>', crud.views.show, name='show'),
    path('crud/new', crud.views.new, name='new'),
    path('crud/edit',crud.views.edit, name ="edit"),
    path('blogupdate/<int:post_id>',crud.views.blogupdate, name='blogupdate'),
    path('delete/<int:post_id>',crud.views.delete,name='delete'),
    path('crud/mypage',crud.views.mypage, name='mypage'),
    path('crud/joinList', crud.views.joinList, name='joinList'),
    path('crud/search',crud.views.search,name='search'),
    path('join/<int:post_id>',crud.views.join, name='join'),
    path('like/<int:post_id>',crud.views.like, name='like'),

    path('crud/pay', crud.views.pay, name='pay'),

    path('kakaopay/', include('kakaopay.urls')),
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
