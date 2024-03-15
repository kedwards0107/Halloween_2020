import RPi.GPIO as GPIO
import time
from multiprocessing import Process
import gspread
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope) #creds.json not saved on github for security
client = gspread.authorize(creds)
sheet = client.open("Halloween").sheet1  # Open the spreadsheet

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define sleep times
SleepTimeS = 0.2
SleepTimeL = 0.5

# Define control pins for two sets of GPIOs
ControlPin = [20, 21, 17, 27]
ControlPin2 = [18, 23, 24, 25]

# Function to set up pins
def setup_pins(pins):
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

# Set up all control pins
setup_pins(ControlPin)
setup_pins(ControlPin2)

# Define stepper motor sequences
seq1 = [[1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0],
        [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1]]
seq2 = [[1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0],
        [0, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0]]

# Function to create a blinking pattern
def blink_pattern(pin, duration):
    GPIO.setup(pin, GPIO.OUT)
    for _ in range(duration):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(SleepTimeL)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(SleepTimeL)

# Define functions for each candy
def kitkat():
    blink_pattern(4, 10)

def hershey():
    blink_pattern(13, 10)

def dots():
    blink_pattern(12, 10)

def nerds():
    blink_pattern(26, 10)

# Function to control stepper motor
def control_stepper(ControlPin, sequence, steps):
    for i in range(steps):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin], sequence[halfstep][pin])
            time.sleep(0.001)

# Main loop
try:
    while True:
        for input_pin, action, pins, seq, steps in [
            (22, dots, ControlPin, seq2, 564),
            (16, hershey, ControlPin, seq1, 564),
            (19, kitkat, ControlPin2, seq2, 564),
            (6, nerds, ControlPin2, seq1, 532)
        ]:
            GPIO.setup(input_pin, GPIO.IN)
            input_state = GPIO.input(input_pin)
            if input_state == 1:
                print(action.__name__)
                Process(target=action).start()
                control_stepper(pins, seq, steps)
            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Done")
