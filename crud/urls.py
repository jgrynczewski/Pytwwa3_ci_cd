from django.urls import path

from . import views

app_name = "crud"

urlpatterns = [
    path('message-list', views.MessageList.as_view(), name='message-list'),
    path('message-detail/<int:pk>', views.MessageDetail.as_view(), name='message-detail'),
    path('message-create', views.MessageCreate.as_view(), name='message-create'),
    path('message-update/<int:pk>', views.MessageUpdate.as_view(), name='message-update'),
    path('message-delete/<int:pk>', views.MessageDelete.as_view(), name='message-delete')
]