import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    # Adjust for ambient noise levels
    r.adjust_for_ambient_noise(source)

    # Listen for speech
    audio = r.listen(source)

try:
    # Recognize speech using Google Speech Recognition
    print("You said: " + r.recognize_google(audio))

except sr.UnknownValueError:
    # Speech is unintelligible
    print("Could not understand audio")

except sr.RequestError as e:
    # Unable to access the Google Speech Recognition API
    print("Error: Could not request results from Google Speech Recognition service; {0}".format(e))