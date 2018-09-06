import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Moteur1A = 33     ## premiere sortie du premier moteur, pin 16
Moteur1B = 35      ## deuxieme sortie de premier moteur, pin 18
Moteur1E = 37      ## enable du premier moteur, pin 22
Bouton_In = 31


GPIO.setup(Moteur1A,GPIO.OUT)  ## ces trois pins du Raspberry Pi sont des sorties
GPIO.setup(Moteur1B,GPIO.OUT)
GPIO.setup(Moteur1E,GPIO.OUT)
GPIO.setup(Bouton_In,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm = GPIO.PWM(Moteur1E,50)   ## pwm de la pin 22 a une frequence de 50 Hz
pwm.start(100)   ## on commemnce avec un rapport cyclique de 100%

while 1:

	if (GPIO.input(Bouton_In) == True):
		GPIO.output(Moteur1A,GPIO.HIGH)
		GPIO.output(Moteur1B,GPIO.LOW)
		GPIO.output(Moteur1E,GPIO.HIGH)
		sleep(1)

		GPIO.output(Moteur1A,GPIO.LOW)
		GPIO.output(Moteur1B,GPIO.LOW)
		sleep(1)

		GPIO.output(Moteur1A,GPIO.LOW)
		GPIO.output(Moteur1B,GPIO.HIGH)

		sleep(1)

		GPIO.output(Moteur1A,GPIO.LOW)
		GPIO.output(Moteur1B,GPIO.LOW)
		sleep(1)

GPIO.output(Moteur1E,GPIO.LOW)
pwm.stop()
GPIO.cleanup()

