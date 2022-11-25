from django.shortcuts import render
from django.http import HttpResponse

def index(request,name,interests,age):
    return HttpResponse(f"""
        <h1 style = "font-family:Helvetica">ФИО:{name}</h1>
        <h1 style = "font-family:Helvetica">Возраст:{age}</h1>
        <h1 style = "font-family:Helvetica">Интересы:{interests}</h1>
        <a style = "text-decoration:none;font-family:Helvetica ;font-size: 24px;" href = "http://127.0.0.1:8000/contacts">Contacts</a>
        <a style = "text-decoration:none;font-family:Helvetica ;font-size: 24px;" href = "http://127.0.0.1:8000/about">About</a>
    """)
def about(request,town,learn,like):
    return HttpResponse(f"""
            <h1 style = "font-family:Helvetica">Приехал из {town}</h1>
            <h1 style = "font-family:Helvetica">успеваемость в школе {learn}</h1>
            <h1 style = "font-family:Helvetica">Учиться {like}</h1>
            <a style = "text-decoration:none;font-family:Helvetica ;font-size: 24px;" href = "http://127.0.0.1:8000/contacts">Contacts</a>
                <a style = "text-decoration:none;font-family:Helvetica ;font-size: 24px;" href = "http://127.0.0.1:8000/">Home</a>
        """)
def contacts(request,git,tg,vk):
    return HttpResponse(f"""
                <h1 style = "font-family:Helvetica">Git:<a href = {git}  target = "_blank" style = "text-decoration:none;font-family:Helvetica">{git}</a></h1>
                <h1 style = "font-family:Helvetica">ВК:<a href = {vk} target = "_blank" style = "text-decoration:none;font-family:Helvetica">{vk}</a></h1>
                <h1 style = "font-family:Helvetica">Telegram: {tg}</h1>
                <a style = "text-decoration:none;font-family:Helvetica;font-size: 24px;" href = "http://127.0.0.1:8000/">Home</a>
                <a style = "text-decoration:none;font-family:Helvetica;font-size: 24px;" href = "http://127.0.0.1:8000/about">About</a>
            """)