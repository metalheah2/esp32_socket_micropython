#Main-Webserver
import usocket as socket
from machine import Pin

led=Pin(2,Pin.OUT)
print("Testing")
def web_page():
    if(led.value()==1):
        gpio_state="ON"
    else:
        gpio_state="OFF"
        
    html ="""<HTML><HEAD><center><font size="7">Control de ESP32</font></center></HEAD>
    <TITLE>ESP32</TITLE><BODY>
    <center><font size="6">Led : Prendido</font></center>
    <center>
    <p><font size="6">Estado : <b>""" + gpio_state + """</b></font></p>
    <a href="/?led=on"><button><font size="5"> Prender &#9679 </font></button>
    <a href="/?led=off"><button><font size="5"> Apagar &#9675 </font></button>
    </center>
    </BODY>
    </HTML>"""
    return html
    
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('192.168.0.30',8023))
s.listen(5)

while(True):
    conn,addr=s.accept()
    print("Conexion aceptada de %s"%str(addr))
    request=conn.recv(1024)
    request=str(request)
    print("Content = %s"%request)
    led_on=request.find('/?led=on')
    led_off=request.find('/?led=off')
    if(led_on==6):
        print("LED ON")
        led.value(1)
    if(led_off==6):
        print("LED OFF")
        led.value(0)
    response=web_page()
    conn.send("HTTP/1.1 200 OK\n")
    conn.send("Contect-Type: text/html\n")
    conn.send("Connection: close\n\n")
    conn.sendall(response)
    conn.close()
