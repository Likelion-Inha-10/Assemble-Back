"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from newapp import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.Test.as_view()),
    path('', views.First.as_view()),
    # path('signup/', csrf_exempt(views.Signup.as_view())),
    # path('login/', csrf_exempt(views.Login.as_view())),  #X
    # path('logout/', csrf_exempt(views.Logout.as_view())),    #X
    path('create_tdl/', views.CreateToDoList.as_view()),
    path('delete_tdl/<int:tdl_id>', views.DeletedToDoList.as_view()),
    path('tdl/<int:tdl_id>', views.FindToDoList.as_view()),
    path('tdl/priority/<int:tdl_id>', views.Priority.as_view()),
    path('tdl/end/<int:tdl_id>', views.EndList.as_view()),
    path('main/', views.Main.as_view()),
    path('upload/', views.FileUploadView.as_view()),
    path('download/<int:file_id>', views.FileDownloadView.as_view()),
    path('delete_file/<int:file_id>', views.DeleteFile.as_view()),  #
    path('create_grp/', views.CreateGroup.as_view()),
    path('delete_grp/', views.DeleteGroup.as_view()),
    path('filelists/', views.FileList.as_view()),
    path('create_ntc/', views.CreateNotice.as_view()),  #
    path('delete_ntc', views.DeleteNotice.as_view()),
    path('ntc/<int:ntc_id>', views.FindNotice.as_view()),   #
    # path('logout/', views.Logout.as_view()),

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
