from django.conf.urls import url 
# from user import views
from .views import user_list, user_detail

urlpatterns = [ 
    url(r'^user_list/$', user_list),
    url(r'^user_detail/$', user_detail)
]