import tkinter as tk
import time
import pyautogui
import os, sys
from PIL import Image,ImageTk
import winsound

ISRUN = False
def toggle_geom():
    pass

def updateImg(number, sleepNum):
    imgName = dir+"/BSOD/bsod" + str(number) + ".png"
    img = Image.open(imgName).resize((root.winfo_screenwidth(),root.winfo_screenheight()),Image.LANCZOS)
    bg1 = ImageTk.PhotoImage(img)
    bgimage.configure(image=bg1, cursor='none')
    bgimage.image = bg1
    root.update()
    time.sleep(sleepNum)
def initiate(e):
    global ISRUN
    if ISRUN == False:
        ISRUN = True
        time.sleep(1)
        updateImg(1, 4)
        updateImg(2, 6)
        updateImg(3, 7)
        updateImg(4, 0.5)
        winsound.PlaySound(dir+'/noise1.wav',winsound.SND_ASYNC)
        updateImg(3, 3)
        updateImg(6, 0.01)
        winsound.PlaySound(dir + '/noise3.wav', winsound.SND_ASYNC)
        updateImg(3, 1.5)
        winsound.PlaySound(dir + '/noise2.wav', winsound.SND_ASYNC)
        updateImg(4, 0.1)
        updateImg(3, 0.75)
        winsound.PlaySound(dir + '/final.wav', winsound.SND_ASYNC)
        updateImg(7, 1.5)
        winsound.PlaySound(dir + '/loop.wav', winsound.SND_ASYNC)

time.sleep(5)
dir = os.path.dirname(os.path.abspath(sys.argv[0]))
print(dir)
pyautogui.hotkey("win","d")
if keyboard.is_pressed('alt+f4'):
    simulate_key_press()
time.sleep(0.7)
im=pyautogui.screenshot('desktop.png')
root=tk.Tk()
root.geometry('{}x{}+0+0'.format(root.winfo_screenwidth(),root.winfo_screenheight()))
bg = tk.PhotoImage(file="desktop.png")
bgimage = tk.Label(root, image=bg, width=root.winfo_screenwidth(),height=root.winfo_screenheight(), borderwidth=0)
bgimage.place(x=0, y=0)
bgimage.bind('<Button-1>', initiate)
root.attributes("-fullscreen", True)
root.bind('<Escape>', toggle_geom)
root.attributes("-topmost", True)
root.update()

root.mainloop()