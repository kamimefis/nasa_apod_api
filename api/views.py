from django.shortcuts import render
import requests
from .forms import DateForm
import os

NASA_API_URL= "https://api.nasa.gov/planetary/apod"
NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

def apod_view(request):
    image_data= None

    # Al enviar el formulario, se crea la instancia DateForm con la data recibida
    if request.method == "POST":
        form= DateForm(request.POST)
        if form.is_valid():
            date= form.cleaned_data["date"] #recupera la fecha desde cleaned_data
            # se llama a la api de la nasa y se pasan los parámetros requeridos
            response= requests.get(NASA_API_URL, params={
                "api_key": NASA_API_KEY,
                "date": date,
                "thumbs": True #si el resultado es un video, la API devuelve también una imagen en miniatura
            })
            if response.status_code == 200:
                image_data= response.json()
    
    else:
        form= DateForm()

    return render(request, "api/apod.html", {"form": form, "image_data": image_data})