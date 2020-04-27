
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Bank.views import index, addAccount, updateAccount, deleteAccount, home,   customer, register, loginPage, logOutUser
from setup_for_bank.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logOutUser, name='logout'),
    path('customer/', customer),
    path('index/', index, name='index'),
    path('addAccount/', addAccount, name='addAccount'),
    path('updateAccount/<int:Bank_id>/', updateAccount, name='updateAccount'),
    path('deleteAccount/<int:Bank_id>/', deleteAccount, name='deleteAccount'),
]

if settings.DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
