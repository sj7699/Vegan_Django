from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .import views
from django.conf import settings
from django.conf.urls.static import static

router=DefaultRouter()
router.register(r'product',views.ProductSet)
router.register(r'meal_by_client',views.meal_by_client)
router.register(r'cut_by_price',views.cut_by_price)
router.register(r'user_detail',views.User_DetailSet)
router.register(r'get_meal',views.get_meal_list)
urlpatterns=[
    path('',include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)