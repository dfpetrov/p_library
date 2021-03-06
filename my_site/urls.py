"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from p_library import views
from django.urls import include
from p_library.views import AuthorEdit, BookRentEdit, FriendEdit, AuthorList, FriendList, author_create_many, books_authors_create_many, BookCreate, BookUpdate
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_list', views.book_list),
    path('', views.index),
    path('book_increment/', views.book_increment),
    path('book_decrement/', views.book_decrement),
    
    # Добавляем новый urlpattern /redactions/.
    path('redactions/', views.redactions, name='redactions'),
    path('book_rent_list/', views.book_rent_list, name='book_rent_list'),
    path('friends', FriendList.as_view(), name='friend_list'),

    # path('author/create', views.AuthorEdit.as_view(), name='author_create'),  
    # path('authors', views.AuthorList.as_view(), name='author_list'), 
]

urlpatterns += [  
	path('author/create', AuthorEdit.as_view(), name='author_create'),
	path('authors', AuthorList.as_view(), name='author_list'),  
	path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('book_rent/create', BookRentEdit.as_view(), name='book_rent_create'),
    path('friend/create', FriendEdit.as_view(), name='friend_create'),
    path('book/create', BookCreate.as_view(), name='book_create'),
    url(r'book/update/(?P<pk>\d+)/$', BookUpdate.as_view(), name='book_update'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)