from .import views
from django.urls import path, include

app_name='flipkartapp'
urlpatterns=[
    #path('',include('flipkartapp.urls')),

    path('',views.allproductCat,name='allproductCat'),
    path('<slug:c_slug>/',views.allproductCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views. proDetail,name='prodCatdetail')
]
