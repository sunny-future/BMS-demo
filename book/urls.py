from django.urls import path, re_path
from book import views, sub_query, join_query, fq_query

urlpatterns = [
    path('index/', views.index),
    path('show_book/', views.show_book),
    path('add_book/', views.add_book),
    re_path(r'^delete_book/(?P<id_book>\d+)$', views.delete_book),
    re_path(r'^update_book/(?P<id_book>\d+)$', views.update_book),
    path('show_publish/', views.show_publish),
    path('add_publish/', views.add_publish),
    re_path(r'^delete_publish/(?P<id_publish>\d+)$', views.delete_publish),
    re_path(r'^update_publish/(?P<id_publish>\d+)$', views.update_publish),
    re_path(r'^show_author/$', views.show_author),
    re_path(r'^add_author/$', views.add_author),
    re_path(r'^delete_author/(?P<id_author>\d+)$', views.delete_author),
    re_path(r'^update_author/(?P<id_author>\d+)$', views.update_author),
    re_path(r'^show_author_detail/$', views.show_author_detail),
    re_path(r'^add_author_detail/$', views.add_author_detail),
    re_path(r'^delete_author_detail/(?P<id_author_detail>\d+)$', views.delete_author_detail),
    re_path(r'^update_author_detail/(?P<id_author_detail>\d+)$', views.update_author_detail),
    re_path(r'^e_chart/index/$', views.e_chart_index),
    re_path(r'^sub_query/$', sub_query.sub_query),
    re_path(r'^join_query/$', join_query.join_query),
    re_path(r'^fq_query/$', fq_query.fq_query),

]
