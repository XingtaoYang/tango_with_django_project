from django.shortcuts import render
from django.http import HttpResponse

# HttpResponse 是 Django 中用于向客户端（浏览器）返回响应内容的核心对象
# 它属于 django.http 模块，主要作用是将服务器处理后的内容（文本、HTML、数据等）
# 封装成 HTTP 响应，发送给请求的浏览器。

# 定义首页视图函数：接收浏览器的请求（request参数），返回响应
def index(request):
    return render(request, 'rango/index.html')

def about(request):
    return render(request, 'rango/about.html')