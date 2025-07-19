import speech_recognition as sr

r = sr.Recognizer()

try:
    while True:
        with sr.Microphone() as source:
            print("Meow Says")
            audio = r.listen(source)
            
            try:
                text = r.recognize_google(audio)
                text = text.lower()
                print("Meow", text)
            except sr.UnknownValueError:
                print("Meow couldn't understand audio")
            except sr.RequestError as e:
                print(f"Meow couldn't request results from Google Speech Recognition service; {e}")
except KeyboardInterrupt:
    print("Meow says goodbye!")