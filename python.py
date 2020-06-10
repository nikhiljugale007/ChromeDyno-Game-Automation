import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):    

    for i in range(300, 415):
        for j in range(500, 650):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Game is started please open  chrome")
    time.sleep(2)
    
    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
        
        
    
           
      

