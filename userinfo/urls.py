from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views

router=DefaultRouter()
router.register(r'favor',views.FavorcategorySet)
router.register(r'product',views.ProductSet)
router.register(r'rproduct',views.rlist)
router.register(r'meal_by_client',views.meal_by_client)
router.register(r'cut_by_price',views.cut_by_price)
urlpatterns=[
    path('',include(router.urls)),
]