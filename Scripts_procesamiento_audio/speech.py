import speech_recognition as sr
#import warning

r = sr.Recognizer()
n = len(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=n-1)


with mic as source:
    audio = r.listen(source)

print(r.recognize_google(audio))