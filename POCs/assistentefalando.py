import pyttsx3 # instala a biblioteca pyttsx3

engine = pyttsx3.init()

engine.say ("Hello World")

engine.runAndWait()

engine.stop()
