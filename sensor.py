import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO =24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

file = '/var/www/html/data.txt'
#f =  open(file_path, 'w')

try:

	while True:
		GPIO.output(TRIG,False)
		time.sleep(0.1)
		GPIO.output(TRIG, True)
		time.sleep(0.0001)
		GPIO.output(TRIG, False)
	
		while GPIO.input(ECHO) == 0:
			pulse_start = time.time()

		while GPIO.input(ECHO) == 1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		dist = pulse_duration * 17150
		dist = round(dist, 2)
		
		print("distance:", dist, end='\r', flush=True)
		with open(file,'w') as f:
			f.write(str(dist))

except KeyboardInterrupt:
	print("cleanup")
	GPIO.cleanup()
