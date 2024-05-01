from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),  # type:ignore
    path('search/', views.search, name='search'),  # type:ignore

    # contact (CRUD)
    path('contact/create/', views.contact, name='contact'),  # type:ignore
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),  # type:ignore
    path('contact/<int:contact_id>/update/', views.contact, name='contact'),  # type:ignore
    path('contact/<int:contact_id>/delete/', views.contact, name='contact'),  # type:ignore
]
