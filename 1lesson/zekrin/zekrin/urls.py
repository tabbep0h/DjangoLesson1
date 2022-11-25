from django.contrib import admin
from django.urls import path
from zekrinapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,kwargs = {"name":'Зекрин Тимур Ильдусович.',"age" :"16 лет.","interests":"программирование,сим-рейсинг,милитаризм,аниме."}),
    path("about",views.about,kwargs = {"town":"Пермского края","learn":"хорошая","like":"любит"}),
    path("contacts",views.contacts,kwargs = {"git":"https://github.com/tabbep0h","vk":"https://vk.com/tabbep0h","tg":"@tabbep0h",})
]

