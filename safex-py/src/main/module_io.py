import re
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO

ADC.setup();

def prepareFor(_optarg):
  pin = -1;
  if _optarg is None:
    return -1;

  if _optarg[0] == 'A':
    return -2;

  if _optarg[0] == 'P':
    pin = _optarg;

  if pin == 0:
    return -1;

  return pin;

def readAnalog(optarg):
  ain = ADC.read(optarg);
  return ain;


def read_input(optarg):
  pin = prepareFor(optarg);
  if pin == -1:
    return -1;
  if pin == -2:
    return readAnalog(optarg);
  
  GPIO.setup(pin, GPIO.IN);
  res =  GPIO.input(pin);
  return res

def write_output(optarg):
  pin = prepareFor(optarg).split("=");
  value = pin[1]
  pin = pin[0]
 
  if pin[0] == -1:
    return -1;
 
  if value is None:
    return -1;
  
  GPIO.setup(pin, GPIO.OUT);
  GPIO.output(pin,  GPIO.HIGH if (value==1) else GPIO.LOW);
  return value;

