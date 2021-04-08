import keyboard
import time
import socket
import webbrowser
import tkinter as tk

s=socket.socket()

window=tk.Tk()
iplab=tk.Label(window,text="Enter IP Address of your device")
ipent=tk.Entry(window)
portlab=tk.Label(window,text="Enter Port Number")
portent=tk.Entry(window)
def Connect():
    global s
    host=ipent.get()
    port=int(portent.get())
    s.bind((host,port))
    s.listen(5)
    c,a=s.accept()
    print(a[0])
    URL="http://"+a[0]+":5000"
    webbrowser.open(URL, new=2)
    mes='x'
    while True:
        if (keyboard.is_pressed('a') or keyboard.is_pressed('w') or keyboard.is_pressed('s') or keyboard.is_pressed('d') or keyboard.is_pressed('a+w') or keyboard.is_pressed('w+d') or keyboard.is_pressed('w+a') or keyboard.is_pressed('d+w') or keyboard.is_pressed('s+a') or keyboard.is_pressed('a+s') or keyboard.is_pressed('s+d') or keyboard.is_pressed('d+s') or keyboard.is_pressed('e')):
            key=str(keyboard.get_hotkey_name())
            time.sleep(0.1)
            print(key)
            c.send(str.encode(key))
        elif keyboard.is_pressed('e'):
            key = str(keyboard.get_hotkey_name())
            time.sleep(0.1)
            c.send(str.encode(key))
            c.close()
            window.quit()
            break
        else:
            c.send(str.encode(mes))
            continue

conbut=tk.Button(window,text="Connect",command=Connect)

iplab.grid(row=0,column=0)
ipent.grid(row=0,column=1)
portlab.grid(row=1,column=0)
portent.grid(row=1,column=1)
conbut.grid(row=3,column=1)

window.mainloop()



