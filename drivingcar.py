import time
from fischertechnik.controller.Motor import Motor
from lib.controller import *

x = None
y = None
mindes_distanz = None
Geschwindigkeit = None
z = None
Max_distanz = None
x_check = None
y_check = None
z_check = None


def Richtungs_Entscheidung():
  global x, y, mindes_distanz, Geschwindigkeit, z, Max_distanz, x_check, y_check, z_check
  if x == '0' and y == '2' and z == '0':
    TXT_M_S1_servomotor.set_position(int(45))
    Rückwärtz()
  elif x == '1' and y == '2' and z == '0':
    """
    Links
    """
    TXT_M_S1_servomotor.set_position(int(45))
    Rückwärtz()
  elif x == '2' and y == '2' and z == '0':
    """
    Links
    """
    TXT_M_S1_servomotor.set_position(int(45))
    Rückwärtz()
  elif x == '0' and y == '2' and z == '1':
    """
    Rechts
    """
    TXT_M_S1_servomotor.set_position(int(135))
    Rückwärtz()
  elif x == '0' and y == '2' and z == '2':
    """
    Rechts
    """
    TXT_M_S1_servomotor.set_position(int(135))
    Rückwärtz()
  elif x == '1' and y == '2' and z == '1':
    """
    Rechts
    """
    TXT_M_S1_servomotor.set_position(int(135))
    Rückwärtz()
  elif x == '1' and y == '2' and z == '2':
    """
    Rechts
    """
    TXT_M_S1_servomotor.set_position(int(135))
    Rückwärtz()
  elif x == '2' and y == '2' and z == '1':
    """
    Links
    """
    TXT_M_S1_servomotor.set_position(int(45))
    Rückwärtz()
  elif x == '2' and y == '2' and z == '2':
    """
    Rechts
    """
    TXT_M_S1_servomotor.set_position(int(135))
    Rückwärtz()
  elif x == '2' and y == '0' and z == '0':
    """
    Links
    """
    TXT_M_S1_servomotor.set_position(int(45))
    Rückwärtz()
  elif x == '2' and y == '0' and z == '1':
    """
    Links
    """
    TXT_M_S1_servomotor.set_position(int(45))
    Rückwärtz()
  elif x == '2' and y == '1' and z == '0':
    """
    Links
    """
    TXT_M_S1_servomotor.set_position(int(45))
    Rückwärtz()
  elif x == '2' and y == '1' and z == '1':
    """
    Links
    """
    TXT_M_S1_servomotor.set_position(int(45))
    Rückwärtz()
  elif x == '0' and y == '0' and z == '2':
    """
    Rechts
    """
    TXT_M_S1_servomotor.set_position(int(135))
    Rückwärtz()
  elif x == '1' and y == '0' and z == '2':
    """
    Rechts
    """
    TXT_M_S1_servomotor.set_position(int(135))
    Rückwärtz()
  elif x == '0' and y == '1' and z == '2':
    """
    Rechts
    """
    TXT_M_S1_servomotor.set_position(int(135))
    Rückwärtz()
  elif x == '1' and y == '1' and z == '2':
    """
    Rechts
    """
    TXT_M_S1_servomotor.set_position(int(135))
    Rückwärtz()
  elif x == '0' and y == '1' and z == '0':
    Rechts()
  elif x == '1' and y == '1' and z == '0':
    Links()
  elif x == '0' and y == '1' and z == '1':
    Rechts()
  elif x == '1' and y == '1' and z == '1':
    Gerade()
  elif x == '1' and y == '0' and z == '0':
    Links()
  elif x == '0' and y == '0' and z == '1':
    Rechts()
  elif x == '1' and y == '0' and z == '1':
    Gerade()
  elif x == '0' and y == '0' and z == '0':
    Gerade()


def Sensoren_Check():
  global x, y, mindes_distanz, Geschwindigkeit, z, Max_distanz, x_check, y_check, z_check
  x = '0'
  y = '0'
  z = '0'
  x_check = TXT_M_I5_ultrasonic_distance_meter.get_distance()
  y_check = TXT_M_I2_ultrasonic_distance_meter.get_distance()
  z_check = TXT_M_I3_ultrasonic_distance_meter.get_distance()
  print('Rechts:')
  print(x_check)
  print('Mitte:')
  print(y_check)
  print('Links:')
  print(z_check)
  if x_check <= Max_distanz:
    x = '1'
  if x_check <= mindes_distanz:
    x = '2'
  if y_check <= Max_distanz:
    y = '1'
  if y_check <= mindes_distanz:
    y = '2'
  if z_check <= Max_distanz:
    z = '1'
  if z_check <= mindes_distanz:
    z = '2'
  Richtungs_Entscheidung()


def Setup():
  global x, y, mindes_distanz, Geschwindigkeit, z, Max_distanz, x_check, y_check, z_check
  print('Setup')
  mindes_distanz = 10
  Max_distanz = 40
  Geschwindigkeit = 258


def Rechts():
  global x, y, mindes_distanz, Geschwindigkeit, z, Max_distanz, x_check, y_check, z_check
  TXT_M_M1_motor.set_speed(int(Geschwindigkeit), Motor.CW)
  TXT_M_M1_motor.start()
  TXT_M_S1_servomotor.set_position(int(135))
  print('R')


def Gerade():
  global x, y, mindes_distanz, Geschwindigkeit, z, Max_distanz, x_check, y_check, z_check
  TXT_M_M1_motor.set_speed(int(Geschwindigkeit), Motor.CW)
  TXT_M_M1_motor.start()
  TXT_M_S1_servomotor.set_position(int(90))
  print('G')


def Links():
  global x, y, mindes_distanz, Geschwindigkeit, z, Max_distanz, x_check, y_check, z_check
  TXT_M_M1_motor.set_speed(int(Geschwindigkeit), Motor.CW)
  TXT_M_M1_motor.start()
  TXT_M_S1_servomotor.set_position(int(45))
  print('L')


def Rückwärtz():
  global x, y, mindes_distanz, Geschwindigkeit, z, Max_distanz, x_check, y_check, z_check
  TXT_M_M1_motor.set_speed(int(Geschwindigkeit), Motor.CCW)
  TXT_M_M1_motor.start()
  print('back')


Setup()
TXT_M.get_loudspeaker().play("20_Motor_starting.wav", False)
time.sleep(4)
while True:
  Sensoren_Check()
  time.sleep(0.1)
