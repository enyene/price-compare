from django.urls import path
from .views import ProductListView , product_detail

app_name = 'accounts'

urlpatterns = [
    path('products/',ProductListView.as_view()),
    path('products/<uuid:id>/<slug:product>',product_detail, name='product_detail')
]