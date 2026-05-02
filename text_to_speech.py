import pyttsx3

text = input("Enter the text you want to convert to speech:")

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()