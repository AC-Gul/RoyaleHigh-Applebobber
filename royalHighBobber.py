import pyautogui
import datetime
import random
import time

#print(pyautogui.position())

amountEarned = 0
oldTime = time.perf_counter()

while True:
    screen = pyautogui.screenshot()
    if (pyautogui.locate('AppleBobbingStart.PNG', screen, grayscale=True, confidence=0.8) != None):
        a = random.random()

        try:
            startButtonLocation = pyautogui.locate('AppleBobbingStart.PNG', screen, grayscale=True, confidence=0.8)
            startButtonPoint = pyautogui.center(startButtonLocation)
            pyautogui.moveTo(startButtonPoint[0], startButtonPoint[1], 0.3)
            pyautogui.click(x=startButtonPoint[0], y=startButtonPoint[1], button="left", interval=a)
            pyautogui.moveTo(startButtonPoint[0]+6, startButtonPoint[1]+4, 0.1)
            pyautogui.leftClick()
            pyautogui.click(x=startButtonPoint[0]-1, y=startButtonPoint[1]-3, button="left", interval=a + 0.03)
            time.sleep(5)
        except:
            print("Issue occured with startButton")


        #Shitty error handling
        try:
            #check For bubbles
            while (pyautogui.locate('bubble.PNG', screen, grayscale=True, confidence=0.8)) != None:
                screen = pyautogui.screenshot()
                a = random.random()
                bubbleLocation = pyautogui.locateOnScreen('bubble.PNG', screen, grayscale=True, confidence=0.8)
                bubblePoint = pyautogui.center(bubbleLocation)
                pyautogui.click(button="left", interval=a, x=bubblePoint[0], y=bubblePoint[1])
        except:
            print("WHOOPSIE!!! Bubblefucker failed")
        
               
        
        #click the image
        while (pyautogui.locate('bobbingFinished.PNG', screen, grayscale=True, confidence=0.90)) == None:
               time.sleep(2)
               screen = pyautogui.screenshot()

               # If it's taking too long
               if (oldTime - time.perf_counter() > 120):
                   oldTime = time.perf_counter()
                   amountEarned -= 10
                   break
                
        b = pyautogui.size()
        pyautogui.click(x=600, y=b[1] - 3)
        time.sleep(3)


        print( datetime.datetime.now().strftime("%H:%M:%S") )
        amountEarned += 10
        print("Candies Earned So Far:")
        print(amountEarned)
        print("\n")
        
        
               

    
    
    

