import pyautogui
import keyboard
from docx import Document
from docx.shared import Inches
import win32gui
from PIL import ImageGrab
import time

 # temporary image storage 
# docxfile = "C:/tmp/shots.docx" # main document
hotkey = 's'  # use this combination anytime while script is running

def do_cap():
    x=1
    
    a=int(input('how many screenshots u want to take: '))
    b=int(input('at how much time difference: '))
    
    while x<a+1:
     try:
        print ('Storing capture...')
        shotfile = 'E:\django\hello\image\imgs'+str(x)+'.png'         
        hwnd = win32gui.GetForegroundWindow()  # active window
        bbox = win32gui.GetWindowRect(hwnd)  # bounding rectangle

        # capture screen
        shot = pyautogui.screenshot(region=bbox) # take screenshot, active app
        # shot = pyautogui.screenshot() # take screenshot full screen
        shot.save(shotfile) # save screenshot
        
        # append to document. Doc must exist.
        # doc = Document(docxfile) # open document
        # doc.add_picture(shotfile, width=Inches(7))  # add image, 7 inches wide
        # doc.save(docxfile)  # update document
        print ('Done capture.')
        x+=1
       
        time.sleep(b)
     except Exception as e:  # allow program to keep running
        print("Capture Error:", e)

keyboard.add_hotkey(hotkey, do_cap)  # set hot keys

print("Started. Waiting for", hotkey)

keyboard.wait()   # Block forever
