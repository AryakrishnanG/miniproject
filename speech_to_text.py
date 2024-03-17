import speech_recognition as sr 

def spech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source) # method 
        try:
            voice_data=""
            voice_data = r.recognize_google(audio)
            print(voice_data)
            return voice_data
        except sr.UnknownValueError:
            print("Error: Could not understand audio")
        except sr.RequestError:
            print("Error: Request to Google Speech Recognition service failed")

# Test the function
spech_to_text()
