 #!/usr/bin/python
import RPi.GPIO as GPIO
import time
from multiprocessing import Process

GPIO.setmode(GPIO.BCM)


SleepTimeS = 0.2
SleepTimeL = 0.5

# init list with pin numbers

ControlPin = [20, 21, 17, 27]

ControlPin2 = [18, 23, 24, 25]
# loop through pins and set mode and output to 0

for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)



for pin in ControlPin2:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)


seq1 = [ [1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1] ]


seq2 = [ [1,0,0,1],
	[0,0,0,1],
	[0,0,1,1],
	[0,0,1,0],
	[0,1,1,0],
	[0,1,0,0],
	[1,1,0,0],
	[1,0,0,0] ]

def kitkat():
		GPIO.setup(4,GPIO.OUT)
		GPIO.output(4,GPIO.HIGH)
		#insertRow = [now_format, "sour patch kids",1,0,0,0]
		#sheet.insert_row(insertRow, 2)
		GPIO.output(4, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(4, GPIO.HIGH)
		time.sleep(SleepTimeL)

def hershey():
		GPIO.setup(13, GPIO.OUT)
		GPIO.output(13, GPIO.HIGH)
		#insertRow = [now_format, "sour patch kids",1,0,0,0]
		#sheet.insert_row(insertRow, 2)
		GPIO.output(13, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(13, GPIO.HIGH)
		time.sleep(SleepTimeL)

def dots():
		GPIO.setup(12, GPIO.OUT)
		GPIO.output(12, GPIO.HIGH)
		#insertRow = [now_format, "sour patch kids",1,0,0,0]
		#sheet.insert_row(insertRow, 2)
		GPIO.output(12, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(12, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(12, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(12, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(12, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(12, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(12, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(12, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(12, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(12, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(12, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(12, GPIO.HIGH)
		time.sleep(SleepTimeL)


def nerds():
		GPIO.setup(26, GPIO.OUT)
		GPIO.output(26, GPIO.HIGH)
		#insertRow = [now_format, "sour patch kids",1,0,0,0]
		#sheet.insert_row(insertRow, 2)
		GPIO.output(26, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.HIGH)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.LOW)
		time.sleep(SleepTimeL)
		GPIO.output(26, GPIO.HIGH)
		time.sleep(SleepTimeL)
try:
        while True:

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(22, GPIO.IN)
		input_state = GPIO.input(22)
        if input_state == 0:
			print("Boom boom Bill")
		elif input_state ==1:
			print("dots")
			Process(target=dots).start()
			for i in range(564):
				for halfstep in range(8):
					for pin in range(4):
						GPIO.output(ControlPin[pin], seq2[halfstep][pin])
					time.sleep(0.001)
			for i in range(564):
				for halfstep in range(8):
					for pin in range(4):
						GPIO.output(ControlPin[pin], seq1[halfstep][pin])
					time.sleep(0.001)

			time.sleep(0.1)


		GPIO.setmode(GPIO.BCM)
		GPIO.setup(16, GPIO.IN)
		input_state = GPIO.input(16)
        if input_state == 0:
			print("Boom boom Bill")
		elif input_state ==1:
			print("hershey")
			Process(target=hershey).start()
			for i in range(564):
				for halfstep in range(8):
					for pin in range(4):
						GPIO.output(ControlPin[pin], seq1[halfstep][pin])
					time.sleep(0.001)
			for i in range(564):
				for halfstep in range(8):
					for pin in range(4):
						GPIO.output(ControlPin[pin], seq2[halfstep][pin])
					time.sleep(0.001)
			time.sleep(0.1)

		GPIO.setmode(GPIO.BCM)
        GPIO.setup(19, GPIO.IN)
		input_state = GPIO.input(19)
        if input_state == 0:
			print("Boom boom Bill")
		elif input_state ==1:
			print("kitkat")
			Process(target=kitkat).start()
			for i in range(564):
				for halfstep in range(8):
					for pin in range(4):
						GPIO.output(ControlPin2[pin], seq2[halfstep][pin])
					time.sleep(0.001)
			for i in range(564):
				for halfstep in range(8):
					for pin in range(4):
						GPIO.output(ControlPin2[pin], seq1[halfstep][pin])
					time.sleep(0.001)
			time.sleep(0.1)


		GPIO.setmode(GPIO.BCM)
		GPIO.setup(6, GPIO.IN)
		input_state = GPIO.input(6)
        if input_state == 0:
			print("Boom boom Bill")
		elif input_state ==1:
			print("nerds")
			Process(target=nerds).start()
			for i in range(532):
				for halfstep in range(8):
					for pin in range(4):
						GPIO.output(ControlPin2[pin], seq1[halfstep][pin])
					time.sleep(0.001)
			for i in range(532):
				for halfstep in range(8):
					for pin in range(4):
						GPIO.output(ControlPin2[pin], seq2[halfstep][pin])
					time.sleep(0.001)
			time.sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()
 	print ("Done")
