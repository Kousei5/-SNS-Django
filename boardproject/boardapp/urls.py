from django.urls import path
from .views import signupfunc, loginfunc, listfunc,logoutfunc,detailfunc,goodfunc,readfunc,BoardCreate,UpdatePost,DeletePost
urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('detail/<int:pk>/update', UpdatePost.as_view(), name='update'),
    path('detail/<int:pk>/delete', DeletePost.as_view(), name='delete'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('reed/<int:pk>', readfunc, name='read'),
    path('create/', BoardCreate.as_view(), name='create')
]
