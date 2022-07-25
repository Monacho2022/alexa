import requests
import pywhatkit
import speech_recognition as sr 
import pyttsx3 as voz
import subprocess as sub
from datetime import datetime

import textblob

#config voz asistente
voice=voz.init()
voices=voice.getProperty('voices')
voice.setProperty('voice',voices[0].id)
voice.setProperty('rate',140)

def say(text):
    voice.say(text)
    voice.runAndWait()

while True:
    recognnizer=sr.Recognizer()
    #activar micro
    with sr.Microphone()as source:
        print("analisando...") 
        audio=recognnizer.listen(source,phrase_time_limit=3)
        
    try:#si se entiende nuetra peticion entramos ala logica p 
        comando=recognnizer.recognize_google(audio, language='es-co')
        print(f'creo que dijiste"{comando}"')
        
        comando=comando.lower()
        comando=comando.split(' ')
        
        if 'alexa' in comando :
            if 'reproduce'in comando:
                comando=("comando")
                say("reproduciendo"+comando)
                pywhatkit.playonyt(comando)
                
            if 'temperatura' in comando:
                comando=("manizales")

                url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=bd4851beffdb36b9ea5e8746ae93d28d&units=metric".format(comando)

                res= requests.get(url)

                data= res.json()
                description= data["weather"][0]["description"]
                temp= data["main"]["temp"]
                say(f'la temperatura de {comando} es{temp}y el tiempo{description}')
                       
            elif 'hora' in comando :
                hora=datetime.now().strftime('%H:%M')
                say(f'son las{hora}')
                
            elif 'fecha' in comando :
                fecha=datetime.now().strftime('%d%M%Y')
                say(f'la fecha es{fecha}')
            
                    
        if'terminar'in comando or 'termina'in comando or 'salir'in comando:
                say('seccion terminada')
                
    except:
        say('no entendi,por favor vuelve a intentarlo')
                
                   

