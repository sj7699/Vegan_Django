from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router=DefaultRouter()
router.register(r'favor',views.FavorcategorySet)
router.register(r'product',views.ProductSet)
router.register(r'rproduct',views.rlist)
urlpatterns=[
    path('',include(router.urls)),
]