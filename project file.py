import pywhatkit
import speech_recognition as sr  # create SR as speech rec.
import pyttsx3
import pyjokes
import wikipedia
import math
global command1, command


listener = sr.Recognizer()
engine = pyttsx3.init()

rate = engine.getProperty('rate')  # getting details of current speaking rate
engine.setProperty('rate', 180)  #change of speed

engine.say('I am Jesus, What may I be of service for?')
engine.runAndWait()

def ask_again():
    engine.say('what else can i do for you')
    engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print("listening...")
            voice = listener.listen(source)  # definition for the voice input
            command = listener.recognize_google(voice)  # this is a google api that recognises the sound passed in and makes it into text
            command = command.lower()
            if 'jesus' in command:
                command = command.replace('jesus', '')
                print(command)
    except:
        pass
    return command

def run_jesus():
    command2 = take_command()
    print(command2)
    if 'play' in command2:
        song = command2.replace('play', '')
        talk('playing' + song)
        (pywhatkit.playonyt('playing' + song))
    elif 'joke' in command2:
        talk(pyjokes.get_joke())
    elif 'go away' in command2:
        quit()
    elif 'x' in command2:
        number1 = command2.replace('what is', '')
        number = number1.replace('x', '*')
        letter_number = str(eval(number))
        talk(letter_number)
    elif '+' in command2:
        number1 = command2.replace('what is', '')
        letter_number = str(eval(number1))
        talk(letter_number)
    elif '-' in command2:
        number1 = command2.replace('what is', '')
        letter_number = str(eval(number1))
        talk(letter_number)
    elif '/' in command2:
        number1 = command2.replace('what is', '')
        letter_number = str(eval(number1))
        talk(letter_number)
    elif 'search for' in command2:
        search = command2.replace('search for','')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'who is' in command2:
        search = command2.replace('who is','')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)

    else:
        talk('please say the command again')






while True:
    run_jesus()
    ask_again()







