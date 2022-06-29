import usocket as socket
from machine import Pin
import network

ssid="c921a1"
password="262462008"

station=network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid,password)

while(station.isconnected()==False):
    pass
    
print("Conexion Exitosa")
print(station.ifconfig())

led=Pin(2,Pin.OUT)
