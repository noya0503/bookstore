from django.urls import path

# 引用這個資料夾中的 views 檔案
from . import views

urlpatterns = [
    path('', views.index, name = "Index"),
    path('<id>/onebook',views.onebook,name="OneBook")
#   path('harrypotter', views.harrypotter, name = "HarryPotter"),
#    path('lordofring', views.lordofring, name = "LordofRing"),
#  path('janeeyre', views.janeeyre, name = "JaneEyre"),
]