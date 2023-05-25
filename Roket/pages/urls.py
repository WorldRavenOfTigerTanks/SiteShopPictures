from django.urls import path
from .views import * # импортируем из контроллера все функции
from django.conf.urls import handler404

urlpatterns = [
	
    path('', main, name='main'),
    path('dostavka/', dostavka, name='dostavka'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category, name='category'),
    path('products/<int:post_categoryid>/', products, name='products'),
    path('posts/<int:post_id>/', view_posts, name='view_posts'),
    path('error404/', error404, name='error404'),
    path('error500/', error500, name='error500'),

]
handler404 = 'pages.views.error404'
