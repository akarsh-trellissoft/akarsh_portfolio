from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',portfolio.views.portfolio,name='home'),
    path('blog/',include('blog.url'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
