from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from post.views import LandingPage
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('post.urls', namespace='post')),
    path('news/', include('news.urls', namespace='news')),
    path('', LandingPage.as_view(), name='landing_page'),
    # path('login/',LoginView.as_view(),name='login'),
    # path('signup/', SignUpView.as_view(), name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)