"""
pip3 install pyttsx3 - converting text to speech
pip3 install wikipedia - to get data from web
pip3 install SpeechRecognition
pip3 install pygame -
pip3 install pyown - OpenWeatherMaps
pip3 install pyaudio - mic interface
sudo apt-get python-pyaudio, espeak
pip3 install gTTS
pip3 install cffi, setuptools, numpy, simpleaudio, wave
"""

import random # to generate random replies
import datetime
import webbrowser
import pyttsx3
import pyowm
import wikipedia
from pygame import mixer
import speech_recognition as sr

import simpleaudio as sa
import wave

from gtts import gTTS
from io import BytesIO

import os

# calibrating the text to speech engine
engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)
#volume = engine.getProperty('volume')
#engine.setProperty('volume', 10.0)
#rate = engine.getProperty('rate')
#engine.setProperty('rate', rate - 25
engine.say('Good Evening.')
engine.runAndWait()

# list of preset questions
greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey']
question = ['How are you?', 'How are you doing?', 'how are you', 'how are you doing']
responses = ['Okay', "I'm fine"]
var1 = ['who made you', 'who created you']
var2 = ['I was created by Kaka right in his computer.', 'Kaka', 'Some guy whom Ill never get to know.']
var3 = ['what time is it', 'what is the time', 'time']
var4 = ['who are you', 'what is your name']
cmd1 = ['open browser', 'open google']
cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
cmd4 = ['open youtube', 'i want to watch a video']
cmd5 = ['tell me the weather', 'weather', 'how is the weather today', 'what about the weather']
cmd6 = ['exit', 'close', 'goodbye', 'nothing']
cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
cmd8 = ['what is you favourite colour', 'what is your favourite color']
cmd9 = ['thank you']
repfr9 = ['youre welcome', 'glad i could help you']

# calibrating the speech_recognition engine

def s2t(text):
    mp3_fp = BytesIO()
    tts = gTTS(text, 'en')
    tts.save('hello.mp3')
#    tts.write_to_fp(mp3_fp)

#    play_obj = sa.play_buffer(mp3_fp, 2, 2, 44100)
#    play_obj.play()
#    play_obj.wait_done()
#    mixer.init()
#    mixer.music.load('mp3_fp')
#    mixer.music.play()


while True:
    i=0
    now = datetime.datetime.now()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me something: ")
        audio = r.listen(source)
        try:
            text="You said:-" + r.recognize_google(audio)
            engine.say(text)
            #s2t(text)
            print(text)

            # Loop code with random and wikipedia
            if r.recognize_google(audio) in greetings:
                random_greeting = random.choice(greetings)
                #s2t(random_greeting)
                engine.say(random_greeting)
                print(random_greeting)
                engine.runAndWait()

            elif r.recognize_google(audio) in question:
                #s2t('I am fine')
                print('I am fine')
                engine.say('I am fine')
                engine.runAndWait()

            elif r.recognize_google(audio) in var1:
                reply = random.choice(var2)
                #s2t(reply)
                print(reply)
                engine.say('I was made by Kaka')
                engine.runAndWait()

            elif r.recognize_google(audio) in cmd9:
                #s2t(random.choice(repfr9))
                print(random.choice(repfr9))
                engine.say(random.choice(repfr9))
                engine.runAndWait()

            elif r.recognize_google(audio) in cmd7:
                reply=random.choice(colrep)
                print(reply)
                #s2t(reply)
                engine.say(reply)
                engine.runAndWait()

            elif r.recognize_google(audio) in cmd8:
                reply=random.choice(colrep)
                print(reply)
                #s2t(reply)
                engine.say(reply)
                engine.runAndWait()

            elif r.recognize_google(audio) in cmd2:
                print('playing music')
                mixer.init()
                mixer.music.load("\home\dsskonuru\Desktop\welshly_arms_legendary_official_audio.mp3")
                mixer.music.play()

            elif r.recognize_google(audio) in var4:
                #s2t('I am Duggi your personal AI assistant')
                print('I am Duggi your personal AI assistant')
                engine.say('I am Duggi your personal AI assistant')
                engine.runAndWait()

            elif r.recognize_google(audio) in cmd4:
                webbrowser.open('www.youtube.com')

            elif r.recognize_google(audio) in cmd6:
                print('see you later')
                #s2t('see you later')
                engine.say('see you later.')
                engine.runAndWait()
                exit()

            elif r.recognize_google(audio) in cmd5:
                owm = pyowm.OWM('3f8e79e03a61b67e4542ef3b9892bd8e')
                observation = owm.weather_at_place('Hyderabad, IN')
                observation_list = owm.weather_around_coords(17.5418, 78.3868)
                w = observation.get_weather()
                w.get_wind()
                w.get_humidity()
                w.get_temperature('celsius')

                print(w)
                #print(w.get_wind())
                print(w.get_humidity())
                print(w.get_temperature('celsius'))

                #s2t(w.get_wind())
                #engine.say(w.get_wind())
                #engine.runAndWait()

                engine.say('humidity')
                #s2t('humidity')
                engine.runAndWait()
                engine.say(w.get_humidity())
                #s2t(w.get_humidity())
                engine.runAndWait()

                engine.say('temperature')
                #s2t('temperature')
                engine.runAndWait()
                engine.say(w.get_temperature('celsius'))
                #s2t(w.get_temperature('celsius'))
                engine.runAndWait()

            elif r.recognize_google(audio) in var3:
                print("Current date and time : ")
                print(now.strftime("The time is %H:%M"))
                engine.say(now.strftime("The time is %H:%M"))
                #s2t(now.strftime("The time is %H:%M"))
                engine.runAndWait()

            #elif r.recognize_google(audio) in cmd1:
            #    webbrowser.open_new('www.google.com')

            elif r.recognize_google(audio) in cmd3:
                jokrep = random.choice(jokes)
                print(jokrep)
                engine.say(jokrep)
                #s2t(jokrep)
                engine.runAndWait()

            else:
                print('please wait')
                engine.say("please wait")
                #s2t('please wait')
                engine.runAndWait()
                print(wikipedia.summary(r.recognize_google(audio)))
                engine.say(wikipedia.summary(r.recognize_google(audio)))
                #s2t(wikipedia.summary(r.recognize_google(audio)))
                engine.runAndWait()
                userInput3 = input("or else search in google")
                webbrowser.open_new('www.google.com/search?q=' + userInput3)

        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I didnt get that.')
            #s2t('I didnt get that.')
            engine.runAndWait()
