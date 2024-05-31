import serial
import time
# from gtts import gTTS
# import pygame
import os
import random

import mago

# Configuración del puerto serial
serial_port = 'COM6'  # Reemplaza 'COMX' con el puerto serial correcto
baud_rate = 9600

random = random.randrange(1,51)

mago.predicciones_del_futuro(random)