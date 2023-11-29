from django.urls import path, re_path
from . import views


urlpatterns = [
    path('user/<str:login>/<str:name_dir>/<str:num_post>', views.info_user), #http://127.0.0.1:8000/task/user/Vlad
    path('user/<str:login>/<str:name_dir>', views.info_user),
    path('user/<str:login>', views.info_user),
    path('user/', views.info_user),
    path('error', views.error)

    # re_path(r'^user/(?P<login>\D+)/(?P<name_dir>\D+)/(?P<num_post>\d+)', views.info_user), #http://127.0.0.1:8000/task/user/Vlad
    # re_path(r'^user/(?P<login>\D+)/(?P<name_dir>\D+)', views.info_user),
    # re_path(r'^user/(?P<login>\D+)', views.info_user),
    # re_path(r'^user/', views.info_user)
    # path('error', views.error)
]
