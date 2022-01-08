"""videostrem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import Categoryview
from . import Showview
from . import Episodeview
from . import Adminview
from . import Userview

urlpatterns = [
    path('admin/', admin.site.urls),
    #category
    path('categoryinterface/',Categoryview.CategoryInterface),
    path('submitcategory',Categoryview.SubmitCategory),
    path('displayallcategories',Categoryview.DisplayAllCategories),
    path('categorybyid/', Categoryview.CategoryById),
    path('editdeletecategorydata/',Categoryview.EditDeleteCategoryData),
    path('editicon', Categoryview.EditIcon),
    path('displayallcategoryjson/', Categoryview.DisplayAllCategoriesJSON),
    #show
    path('showinterface/', Showview.ShowCategory),
    path('submitshow', Showview.Submit),
    path('displayallshows/', Showview.DisplayAllShows),
    path('showbyid/',Showview.ShowById),
    path('editdeleteshowdata/',Showview.EditDeleteShowData),
    path('editposter',Showview.Editposter),
    path('edittrailer',Showview.Edittrailer),
    path('editvideo',Showview.Editvideo),
    path('displayallshowjson/', Showview.DisplayAllShowJSON),
    #Episode
    path('episodes/',Episodeview.Episode),
    path('submitepisode',Episodeview.Submitepisode),
    path('displayallepisodes',Episodeview.DisplayAllEpisodes),
    path('episodebyid/',Episodeview.EpisodeById),
    path('editdeleteepisodedata/',Episodeview.EditDeleteEpisodeData),
    path('editposter',Episodeview.Editposter),
    path('edittrailer',Episodeview.Edittrailer),
    path('editvideo',Episodeview.Editvideo),
    #ADMIN
    path('adminlogin/',Adminview.AdminLogin),
    path('chklogin',Adminview.Checklogin),
    #UserInterface
    path('userview/',Userview.Userview),
    path('preview/',Userview.Preview),
    path('tvpreview/',Userview.Tvshows),
]
