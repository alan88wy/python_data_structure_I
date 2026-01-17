import speech_recognition as sr

r = sr.Recognizer()
with sr.AudioFile("note.wav") as source:
    audio = r.record(source)

text = r.recognize_google(audio)

with open("journal.txt", "w") as f:
    f.write(f"Journal Entry:\n{text}")
