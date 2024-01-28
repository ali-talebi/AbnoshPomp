from django.urls import path 
from .views import show_total_detail_category_product , Show_Detail_Product  , show_product_base_category 

app_name = "PRODUCT"
urlpatterns = [
    path("Show_Detail_Product/<int:id>/" , Show_Detail_Product , name="Show_Detail_Product" ) , 
    path("show_product_base_category/<slug:vorodi>/" , show_product_base_category , name="show_product_base_category" ) , 
    path("show_total_detail_category_product/<slug:vorodi>" , show_total_detail_category_product , name="show_total_detail_category_product")
]