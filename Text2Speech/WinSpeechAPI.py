# coding=utf-8
from time import sleep, time
import winsound
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def endAfter(x):
    # t=0
    # if (x[-1]=='s'):
    #     t=x[1:-1]
    
    text = "read ending after " + str(x) + " second. And read now."
    print(text)
    speaker.Speak(text)
    
    start = time()
    for i in range(x):
        sleep(1 - 0.01)
        winsound.Beep(1900, 10)
    end = time()
    print end - start
    
    speaker.Speak("Reading end.")


# def __main__( ):
x = 60 * 3
endAfter(x)
