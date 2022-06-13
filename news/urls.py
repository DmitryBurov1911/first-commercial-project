from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update/', views.NewUpdateView.as_view(), name='update-view'),
    path('<int:pk>/delete/', views.NewDeleteView.as_view(), name='delete-view'),
    path('mail', views.mail, name='mail'),
    path('success', views.success, name='success'),
    path('armaturi', views.armaturi, name='armaturi'),
    path('balki', views.balki, name='balki'),
    path('round', views.round, name='round'),
    path('listi', views.listi, name='listi'),
    path('profanstil', views.profanstil, name='profanstil'),
    path('setka', views.setka, name='setka'),
    path('trubi', views.trubi, name='trubi'),
    path('ugolok', views.ugolok, name='ugolok'),
    path('colormet', views.colormet, name='colorname'),
    path('trubaarm', views.trubaarm, name='trubaarm'),
    path('zhinkmet', views.zhinkmet, name='zhinkmet'),
    path('nerzstal', views.nerzstal, name='nerzstal'),
    path('sandvich', views.sandvich, name='sandvich')
]