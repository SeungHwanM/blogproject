from django.contrib import admin
from django.urls import path, include
import myblog.views
import portfolio.views
import account.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myblog.views.home, name="home"),
    path('blog/', include('myblog.urls')),
    path('blog/portfolio/', include('portfolio.urls')),
    path('blog/account/', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
