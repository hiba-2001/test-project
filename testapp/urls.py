from django.urls import path

from testapp import views

urlpatterns = [
      path('',views.home,name='home'),
      path('student_sign',views.student_sign,name='student_sign'),
      path('admin_sign',views.admin_sign,name='admin_sign'),
      path('login_page', views.login_page, name='login_page'),
      path('student_page', views.student_page, name='student_page'),
      path('student_view', views.student_view, name='student_view'),
      path('admin_page', views.admin_page, name='admin_page'),
      path('student_view', views.student_view, name='student_view'),
      path('add_mark', views.add_mark, name='add_mark'),
      path('view_mark', views.view_mark, name='view_mark'),
      path('view_stud_mark', views.view_stud_mark, name='view_stud_mark'),
      path('view_profile', views.view_profile, name='view_profile'),
      path('mark_update/<int:id>/', views.mark_update, name='mark_update'),
      path('mark_delete/<int:id>/', views.mark_delete, name='mark_delete'),
      path('logout_page', views.logout_page, name='logout_page'),
      path('update_profile', views.update_profile, name='update_profile'),

]