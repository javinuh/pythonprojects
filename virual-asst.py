import speech_recognition as sr
import os
from gtts import gTTS
import warnings
import random
from playsound import playsound

#ignore warning msg
warnings.filterwarnings('ignore')

#record audio
def recordAudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    data = ''
    try:
        data = r.recognize_google(audio)
        print('please wait...')
    except sr.UnknownValueError:
        print('google speech recognition could not understand')
    except sr.RequestError as e:
        print('request Error'+e)
    return data

def assistantResponse(text):
    print('please wait...')
    myobj = gTTS(text=text,lang='en',slow=False)
    myobj.save('assistant_response.mp3')
    playsound('assistant_response.mp3')
def wakeWord(text):
    WAKE_WORD = ['hey','hey assistant','darling']
    text=text.lower()
    for pharse in WAKE_WORD:
        if pharse in text:
            return True
    return False
def greeting(text):
    javith = "say somthing about javith"
    nuhman = "who is nuhman"
    nirose = "tell about nirose"
    u = 'hey who are you'
    thank = 'thank you'
    if text.lower() in u:
            return 'i am javith\'s virtual assistant. how can i help you'
    for word in text.split():
        
        if word.lower() in javith:
            return 'javith is my owner. he is awesome guy. he is very smart person. javith\' character is very good.'
        elif word.lower() in nuhman:
            return 'nuhman is javith\'s best friend. he is awesome guy. he have a very good character. he always support javith.'
        elif word.lower() in nirose:
            return 'nirose is javith\'s best friend. he is wonderful guy. he is javith\'s one of the favourite person.'
        elif word.lower() in thank:
            return 'always welcome sir do not say thank for next time because i am your assistant.'
    return ''
while True:
    text = recordAudio()
    response = ''
    if(wakeWord(text)==True):
        response = response + greeting(text)

        
    assistantResponse(response)