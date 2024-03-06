from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS import TextToAudioStream, SystemEngine
import logging



def process_text(text):
    print (text)
    match text :
        case "Stop toi !" | "Stop toi." | "Stoptois !" | "Stop tour." | "Stop-toi.":
            stream.feed("D'accord, je m'arrete !!!").play()
            recorder.shutdown()
        case "Parle !" | "Parle.":
            stream.feed("Bonjour, je parle beaucoup car je suis une personne sympa").play_async()
        case "Stop !" | "Stop.":
            stream.stop()

        
def recording_started():
    if not stream.stream_running :
        stream.feed("Oui ?!").play()
    else :
        print("J'écoute ...")

    
def recording_finished():
    print("Speech end detected... transcribing...")

if __name__ == '__main__':

    recorder = AudioToTextRecorder(spinner=False, level=logging.INFO, model="medium", language="fr", wake_words="jarvis", on_wakeword_detected=recording_started, on_recording_stop=recording_finished)
    
    engine = SystemEngine("Microsoft Hortense Desktop - French") # replace with your TTS engine
    stream = TextToAudioStream(engine)
    
    while not recorder.is_shut_down :
        recorder.text(process_text)