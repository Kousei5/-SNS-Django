from django.contrib import admin
from django.urls import path, include
from .views import BookList, BookDetail, BookCreate, BookDelete, BookUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', BookList.as_view(), name='list'),
    path('detail/<int:pk>', BookDetail.as_view(), name='detail'),
    path('add/', BookCreate.as_view(), name='add'),
    path('delete/<int:pk>', BookDelete.as_view(), name='delete'),
    path('update/<int:pk>', BookUpdate.as_view(), name='update'),
]
