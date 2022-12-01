import pyautogui
import datetime
import random
import time

#print(pyautogui.position())

# Variable declarations
amountEarned = 0
oldTime = time.perf_counter()

# Main loop
while True:
    
    # Take a screenshot
    screen = pyautogui.screenshot()
    
    # Checks to see if button is visible
    if (pyautogui.locate('AppleBobbingStart.PNG', screen, grayscale=True, confidence=0.8) != None):
        a = random.random() # Random button to avoid potential cheat detection

        # Error handling in case something goes wrong
        try:
            startButtonLocation = pyautogui.locate('AppleBobbingStart.PNG', screen, grayscale=True, confidence=0.8) # Finds the start button
            startButtonPoint = pyautogui.center(startButtonLocation) # Gets the center of the button
            pyautogui.moveTo(startButtonPoint[0], startButtonPoint[1], 0.3) # Moves the mouse cursor to the button
            pyautogui.click(x=startButtonPoint[0], y=startButtonPoint[1], button="left", interval=a) # Clicks the button
            pyautogui.moveTo(startButtonPoint[0]+6, startButtonPoint[1]+4, 0.1) 
            pyautogui.leftClick() # Clicks a second time in case the first click failed
            pyautogui.click(x=startButtonPoint[0]-1, y=startButtonPoint[1]-3, button="left", interval=a + 0.03) # Clicks a third time
            time.sleep(5) # Waits five seconds
        except:
            print("Issue occured with startButton")


        # error handling
        try:
            #check For bubbles
            while (pyautogui.locate('bubble.PNG', screen, grayscale=True, confidence=0.8)) != None:
                screen = pyautogui.screenshot() # Updates the screenshot
                a = random.random() # Get a random number for click interval
                
                # Gets bubble location
                bubbleLocation = pyautogui.locateOnScreen('bubble.PNG', screen, grayscale=True, confidence=0.8)
                bubblePoint = pyautogui.center(bubbleLocation) # Gets the center of the bubble
                pyautogui.click(button="left", interval=a, x=bubblePoint[0], y=bubblePoint[1]) # Clicks bubble
        except:
            print("WHOOPSIE!!! Bubbleclicker failed") # In case something fails with image detection
        
               
        
        # Wait for the finished flag to appear
        while (pyautogui.locate('bobbingFinished.PNG', screen, grayscale=True, confidence=0.90)) == None:
               time.sleep(2) # Wait 2 seconds
               screen = pyautogui.screenshot() # Take a screenshot to update screen

               # If it's taking longer than 2 minutes, reiterate
               if (oldTime - time.perf_counter() > 120):
                   oldTime = time.perf_counter()
                   amountEarned -= 10 # reduce amount earned to accomodate later accumalatoin
                   break
                
        b = pyautogui.size() # Gets the screen size
        pyautogui.click(x=600, y=b[1] - 3) # Clicks the bottom bar of the screen
        time.sleep(3) # Wait 3 seconds

        # Output updates
        print( datetime.datetime.now().strftime("%H:%M:%S") ) # Print out the current time
        amountEarned += 10 # Increase amounnt earned
        
        # Format out print statements
        print("Candies Earned So Far:")
        print(amountEarned)
        print("\n")
        
        
               

    
    
    

