from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html",context = {"name":'Зекрин Тимур Ильдусович.',"age" :"16 лет.","interests":"программирование,сим-рейсинг,милитаризм,аниме."})
def about(request):
    return render(request, "about.html",context = {"town":"Перми","learn":"хорошая","like":"любит"})
def contacts(request):
    return render(request, "contacts.html",context = {"git":"https://github.com/tabbep0h","vk":"https://vk.com/tabbep0h","tg":"@tabbep0h",})