from gtts import gTTS
import playsound, os

class TTS():
    def __init__(self):
        pass

    def speak(self, message: str) -> None:
        if message == "" or message == None:
            return
        
        tts = gTTS(text=message, lang="en")
        tts.save("output.mp3")
        
        playsound.playsound("output.mp3")

        os.remove("output.mp3")