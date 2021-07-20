from playsound import playsound
import datetime
import pyttsx3


def speak(text):     # making speak function to speak message
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def alarm_clock():
    time_of_ring = input("set alarm in (hh/mm) format: ")
    mess = input("Enter messages which you want: ")  # message = which is speak by clock to you
    print("Its ring at given time ................................................")
    while True:
        current_datetime = datetime.datetime.now()
        current_time = current_datetime.time()
        n_time = time_of_ring.split("/")
        h = int(n_time[0])
        m = int(n_time[1])
        time_of_alarm_start = datetime.time(h, m, 0, 0)

        if current_time.hour == time_of_alarm_start.hour and current_time.minute == time_of_alarm_start.minute:
            n = 0
            while n < 5:      # repetition of message
                # if you want to play particular sound at alarm enter path of sound file with wav extension
                # playsound(r"C:\Users\saif\Downloads\Project source file\mixkit-facility-alarm-sound-999.wav")
                speak(f"Sir Its {str(h)} {str(m)} O clock")  # Its speak time
                speak(mess)
                n += 1

                # check = input("Enter stop or s: ")

            break


alarm_clock()

