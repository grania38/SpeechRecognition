import os
import gtts
import speech_recognition as sr
from playsound import playsound

ACTIVATION_COMMAND = "Hey Riri"
rec = sr.Recognizer()

def play_sound(text):

    try:
        tts = gtts.Gtts(text)
        tempfile = "./temp.mp3"
        tts.save(tempfile)
        playsound(tempfile)
        os.remove(tempfile)
    except AssertionError:
        print("Could not play the sound. Try again!")

def get_sound():
    with sr.Microphone() as source:
        print("say something I am giving up on you!")
        audio = rec.listen(source)
    return audio


def sound_to_text(audio):
    text = ""
    try:
        text = rec.recognize_google(audio)
    except sr.UnknownValueError:
        print("Can not understand the audio. Try again!")
    except sr.RequestError:
        print("Could not request from API. Try again!")
    return text

if __name__=="__main__":
    a = get_sound()
    result = sound_to_text(a)

    if ACTIVATION_COMMAND in result.lower():
        print("Activated")
        playsound("How can I help you?")
        note = get_sound()
        note = sound_to_text(note)

        if (note):
            play_sound(note)