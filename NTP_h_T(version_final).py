import datetime

import RPi.GPIO as GPIO
from time import sleep

#import avanceRapide.py

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Moteur1A = 33     ## premiere sortie du premier moteur, pin 16
Moteur1B = 35      ## deuxieme sortie de premier moteur, pin 18
Moteur1E = 37      ## enable du premier moteur, pin 22

GPIO.setup(Moteur1A,GPIO.OUT)  ## ces trois pins du Raspberry Pi sont des sorties
GPIO.setup(Moteur1B,GPIO.OUT)
GPIO.setup(Moteur1E,GPIO.OUT)

pwm = GPIO.PWM(Moteur1E,50)   ## pwm de la pin 22 a une frequence de 50 Hz
pwm.start(100)   ## on commemnce avec un rapport cyclique de 100%



def impulsionDoubleRapide():
    GPIO.output(Moteur1A,GPIO.HIGH)
    GPIO.output(Moteur1B,GPIO.LOW)
    sleep(0.2)

    GPIO.output(Moteur1A,GPIO.LOW)
    GPIO.output(Moteur1B,GPIO.LOW)
    sleep(0.2)

    GPIO.output(Moteur1A,GPIO.LOW)
    GPIO.output(Moteur1B,GPIO.HIGH)
    sleep(0.2)

    GPIO.output(Moteur1A,GPIO.LOW)
    GPIO.output(Moteur1B,GPIO.LOW)
    sleep(0.2)

def impulsionSimplePositifRapide():
    GPIO.output(Moteur1A,GPIO.HIGH)
    GPIO.output(Moteur1B,GPIO.LOW)
    sleep(0.2)

    GPIO.output(Moteur1A,GPIO.LOW)
    GPIO.output(Moteur1B,GPIO.LOW)
    sleep(0.2)

def impulsionDoubleMinutePos():
    GPIO.output(Moteur1A,GPIO.LOW)
    GPIO.output(Moteur1B,GPIO.LOW)
    sleep(59.8)

    GPIO.output(Moteur1A,GPIO.HIGH)
    GPIO.output(Moteur1B,GPIO.LOW)
    sleep(0.2)

    GPIO.output(Moteur1A,GPIO.LOW)
    GPIO.output(Moteur1B,GPIO.LOW)
    sleep(59.8)

    GPIO.output(Moteur1A,GPIO.LOW)
    GPIO.output(Moteur1B,GPIO.HIGH)
    sleep(0.2)

def impulsionDoubleMinuteNeg():

    GPIO.output(Moteur1A,GPIO.LOW)
    GPIO.output(Moteur1B,GPIO.LOW)
    sleep(59.8)

    GPIO.output(Moteur1A,GPIO.LOW)
    GPIO.output(Moteur1B,GPIO.HIGH)
    sleep(0.2)

    GPIO.output(Moteur1A,GPIO.LOW)
    GPIO.output(Moteur1B,GPIO.LOW)
    sleep(59.8)

    GPIO.output(Moteur1A,GPIO.HIGH)
    GPIO.output(Moteur1B,GPIO.LOW)
    sleep(0.2)


date = datetime.datetime.now()
dateHorloge = date.replace(hour=0,minute=0)

print(date.hour)
print(date.minute)

print(dateHorloge.hour)
print(dateHorloge.minute)
heureActuel = datetime.datetime.now()

minuteHorloge=0
heureHorloge=8

minute=0
flag=0

tempsEnMinute = (heureActuel.minute + (60 * (heureActuel.hour%12)))
print("il est %s" % tempsEnMinute)
nbImpulsion=0

while True :
    while (minute != (heureActuel.minute + (60 * (heureActuel.hour%12)))):
        
        print("il est %s %s " % (heureActuel.hour,heureActuel.minute))
        print("mon horloge est à %s" % (minute))


        if((heureActuel.minute + (60 * (heureActuel.hour%12))) - minute == 1):
            print("impaire")
            impulsionSimplePositifRapide()
            flag = 1
            minute=minute+1
            nbImpulsion=nbImpulsion+1  

        else :
            impulsionDoubleRapide()
            minute = minute + 2
            nbImpulsion=nbImpulsion+2

        heureActuel = datetime.datetime.now()  
        dateHorloge = dateHorloge.replace(minute=minuteHorloge)

    print("nb minute %s" % minute)
    print("nbImpulsion%s"%nbImpulsion)
    if(flag==1):
        impulsionDoubleMinuteNeg()
        print("il est %s %s " % (heureActuel.hour,heureActuel.minute))
        print("mon horloge est à %s" % (minute))

    else:
        impulsionDoubleMinutePos()
        print("il est %s %s " % (heureActuel.hour,heureActuel.minute))
        print("mon horloge est à %s" % (minute))



print("l' horloge est à l'heure")
print("il fallait atteindre %s" % minute)
GPIO.output(Moteur1E,GPIO.LOW)
pwm.stop()
GPIO.cleanup()

    # GPIO.output(Moteur1E,GPIO.HIGH)
    # if(date.hour == 1 or date.hour == 13):
    #     print("il est 13h")
    #     while (i <= 30):
    #         print(i)
    #         GPIO.output(Moteur1A,GPIO.HIGH)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         GPIO.output(Moteur1E,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)
    #         i=i+1

    # elif(date.hour == 2 or date.hour == 14):
    #     print("il est 14h")
    #     while i<=60:
    #         print(i)            
    #         GPIO.output(Moteur1A,GPIO.HIGH)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         GPIO.output(Moteur1E,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.HIGH)

    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)
    #         i=i+1

    # elif(date.hour == 3 or date.hour == 15):
    #     print("il est 15h")
    #     while i<=90:
    #         print(i)
    #         GPIO.output(Moteur1A,GPIO.HIGH)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         GPIO.output(Moteur1E,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)
    #         i=i+1

    # elif(date.hour == 4 or date.hour == 16):
    #     print("il est 16h")
    #     while i<=120:
    #         print(i)
    #         GPIO.output(Moteur1A,GPIO.HIGH)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         GPIO.output(Moteur1E,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.HIGH)

    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)
    #         i=i+1

    # elif(date.hour == 5 or date.hour == 17):
    #     print("il est 17h")
    #     while i<=150:
    #         print(i)
    #         GPIO.output(Moteur1A,GPIO.HIGH)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         GPIO.output(Moteur1E,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.HIGH)

    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)
    #         i=i+1

    # elif(date.hour == 6 or date.hour == 18):
    #     print("il est 18h")
    #     while i<=180:
    #         print(i)
    #         GPIO.output(Moteur1A,GPIO.HIGH)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         GPIO.output(Moteur1E,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.HIGH)

    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)
    #         i=i+1

    # elif(date.hour == 7 or date.hour == 19):
    #     print("il est 19h")
    #     while i<=210:
    #         print(i)
    #         GPIO.output(Moteur1A,GPIO.HIGH)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         GPIO.output(Moteur1E,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.HIGH)

    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)
    #         i=i+1

    # elif(date.hour == 8 or date.hour == 20):
    #     print("il est 20h")
    #     while i<=240:
    #         print(i)
    #         GPIO.output(Moteur1A,GPIO.HIGH)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         GPIO.output(Moteur1E,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.HIGH)

    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)
    #         i=i+1

    # elif(date.hour == 9 or date.hour == 21):
    #     print("il est 21h")
    #     while i<=270:
    #         print(i)
    #         GPIO.output(Moteur1A,GPIO.HIGH)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         GPIO.output(Moteur1E,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.HIGH)

    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)
    #         i=i+1
            
    # elif(date.hour == 10 or date.hour == 22):
    #     print("il est 22h")
    #     while i<=300:
    #         print(i)
    #         GPIO.output(Moteur1A,GPIO.HIGH)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         GPIO.output(Moteur1E,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.HIGH)

    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)
    #         i=i+1

    # elif(date.hour == 11 or date.hour == 23):
    #     print("il est 23h")
    #     while i<=330:
    #         print(i)
    #         GPIO.output(Moteur1A,GPIO.HIGH)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         GPIO.output(Moteur1E,GPIO.HIGH)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.HIGH)

    #         sleep(0.2)

    #         GPIO.output(Moteur1A,GPIO.LOW)
    #         GPIO.output(Moteur1B,GPIO.LOW)
    #         sleep(0.2)
    #         i=i+1


