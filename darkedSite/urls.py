from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from posts import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('about/', views.about),
    path('', post_views.posts_list, name="home")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)