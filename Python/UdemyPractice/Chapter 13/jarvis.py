import pyttsx3
import speech_recognition as sr
import  pywhatkit
import yfinance as yf
import pyjokes
import wikipedia
import webbrowser
import datetime

#audio transform into text by microphone

def text_audio_transform_into_text():
    #storeed variable

    r= sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold=0.8
        #record start
        print("say something")
        #store info as audio
        audio=r.listen(source)
        #record stop
        try:
            #search in google
            text=r.recognize_google(audio, language="es-mx")
            #enter in google
            print("tu dijistes " +text)
            return text
        except sr.UnknownValueError:
            print("I didn't get that")
            return "waiting for"

        #dont catch the text
        except sr.RequestError as e:
            print(e)
            print('no hay servicio')
            return "waiting for"


        #unexpected error
        except:
            print("Algo salio mal")
            return "waiting for"

#text to voice for assistent

def text_to_voice(text):
    #engine power on
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# today dayt

def today_dayt():
    today = datetime.date.today()
    print(today)

    week_day = today.weekday()

    if week_day == 0:
        week_day = "Lunes"
    elif week_day == 1:
        week_day = "Martes"
    elif week_day == 2:
        week_day = "Miercoles"
    elif week_day ==3:
        week_day = "Jueves"
    elif week_day == 4:
        week_day = "Viernes"
    elif week_day == 5:
        week_day = "Sabado"
    else:
        week_day = "Domingo"
    text_to_voice(f'Hoy es {week_day}')

#informar la hora

def time_today():
    hora = datetime.datetime.now()
    hora = hora.strftime("%H:%M:%S")
    text_to_voice(f'La hora es {hora}')

#greetings  traveler

def greetings_traveler():

    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour>19:
        moment ='Buenas Noches '
    elif 6 <= hora.hour < 13:
        moment ='Buenos Dias '
    else:
        moment ='Buenas Tardes  '
    text_to_voice(f'{moment} aiooo, bienvenido puerquito soy jarvis')


#central funtion
def jarvis():
    #initial greetings
    greetings_traveler()

    #var for exit program
    exit_program = True

    while exit_program:
        # ask for text
        order =text_audio_transform_into_text().lower()


        if 'abrir youtube' in order:

            text_to_voice("Estoy abriendo Yourube aguanta ")
            webbrowser.open('https://www.youtube.com/watch?v=baaNwRAhHBo&ab_channel=%28G%29I-DLE%28%EC%97%AC%EC%9E%90%29%EC%95%84%EC%9D%B4%EB%93%A4%28OfficialYouTubeChannel%29')
            continue
        elif 'abrir navegador ' in order:
            text_to_voice("Estoy abriendo el navegador aguanta ")
            webbrowser.open('https://www.google.com/')
            continue
        elif 'que dia es hoy ' in order:
            today_dayt()
            continue
        elif 'que hora es ' in order:
            time_today()
            continue

        elif 'buscar en wikipedia' in order:
            text_to_voice("Estoy buscando en wikipedia aguanta ")
            order = order.replace('buscar en wikipedia','')
            wikipedia.set_lang('es')
            result =wikipedia.summary(order,sentences=1)
            text_to_voice('Wikipedia dice')
            text_to_voice(result)
            continue
        elif 'buscar en internet ' in order:
            text_to_voice("Empece la busqueda")
            order = order.replace('buscar en internet', '')
            pywhatkit.search(order)
            text_to_voice('Esto es lo que encontre ')
            continue
        elif 'reproducir' in order:
            text_to_voice("que rolon,  empiezo a reproducirlo")
            pywhatkit.playonyt(order)
        elif "chiste" in order:
            text_to_voice(pyjokes.get_joke('es'))
            continue
        elif 'adiós jarvis' in order:
            text_to_voice('Me voy a mimir aiooo')
            exit_program = False
            continue
jarvis()