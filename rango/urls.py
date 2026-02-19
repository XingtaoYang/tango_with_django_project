
# 导入新版URL工具
from django.urls import path
# 导入rango的视图
from rango import views

# urlpatterns是列表，用path定义URL规则
urlpatterns = [
    # 路径为空字符串（对应首页），关联views.index视图，命名为'index'
    path('', views.index, name='index'),
    path('about/', views.about, name = 'about'),
]
