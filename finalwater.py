import time
from sense_hat import SenseHat

sense=SenseHat()
#this code sets variables to some of the basic colors that the sensehat
#can display. It makes it easier to set colors because you only have to set the numbers once
r = [255,0, 0]
o = [255, 127, 0]
y = [255, 255, 0]
g = [0, 255, 0]
b = [0,0,255]
i = [75, 0, 130]
v = [ 159, 0,255]
e = [0,0,0]

x = 1 #sets first x value which is the condition under which each if
#and while statement runs for the first part of the code
while x == 1:

    image = [e,e,e,e,e,e,e,e,
             e,e,e,e,e,e,e,e,
             r,e,e,e,e,e,e,r,
             r,e,e,e,e,e,e,r,
             r,e,e,e,e,e,e,r,
             r,e,e,e,e,e,e,r,
             r,e,e,e,e,e,e,r,
             r,r,r,r,r,r,r,r,] # sets light color for each light on the senseHAT 8x8

    sense.set_pixels(image) #sets the image code onto the senseHAT
    time.sleep(.15) # stops the code from running for .15 seconds
    x = 1+1 #adds 1 to x so that the next if statement will run

    if x == 2: # if statement dependent on the previous x equation directly above

         image = [e,e,e,e,e,e,e,e,
                  e,e,e,e,e,e,e,e,
                  r,e,e,e,e,e,e,r,
                  r,e,e,e,e,e,e,r,
                  r,e,e,e,e,e,e,r,
                  r,e,e,e,e,e,e,r,
                  r,b,e,e,e,e,e,r,
                  r,r,r,r,r,r,r,r,]

    sense.set_pixels(image)
    time.sleep(.15)
    x = 2 + 1


    if x == 3:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

    sense.set_pixels(image)
    time.sleep(.15)
    x = 3 + 1

    if x == 4:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 4 + 1

    if x == 5:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,b,e,e,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 5 + 1

    if x == 6:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,b,b,e,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 6 + 1

    if x == 7:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 7 + 1

    if x == 8:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,e,e,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 8 + 1

    if x == 9:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 9 + 1

    if x == 10:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 10 + 1

    if x == 11:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 11 + 1

    if x == 12:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,b,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 12 + 1

    if x == 13:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,b,b,e,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 13 + 1

    if x == 14:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 14 + 1

    if x == 15:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,e,e,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 15 + 1

    if x == 16:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 16 + 1

    if x == 17:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 17 + 1

    if x == 18:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,b,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 18 + 1

    if x == 19:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,b,b,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 19 + 1

    if x == 20:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 20 + 1

    if x == 21:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,b,e,e,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 21 + 1

    if x == 22:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 22 + 1

    if x == 23:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 23 + 1

    if x == 24:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,b,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 24 + 1

    if x == 25:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,b,b,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 25 + 1

    if x == 26:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 26 + 1

    if x == 27:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,b,e,e,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 27 + 1

    if x == 28:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,b,b,e,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 28 + 1

    if x == 29:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 29 + 1

    if x == 30:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,b,b,b,b,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 30 + 1

    if x == 31:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,b,b,b,b,b,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 31 + 1

    if x == 32:
        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]
        sense.set_pixels(image)
        time.sleep(.15)
        x = 32 + 1
        #At this point, the cup has been filled and is ready to be poured out.
        #In the next section of code, the water can be poured out by holding the sensehat
        # perfectly upright and tilting it carefully to the left.

from sense_hat import SenseHat

sense=SenseHat()
#this code sets variables to some of the basic colors that the sensehat
#can display. It makes it easier to set colors because you only have to set the numbers once
r = [255,0, 0]
o = [255, 127, 0]
y = [255, 255, 0]
g = [0, 255, 0]
b = [0,0,255]
i = [75, 0, 130]
v = [ 159, 0,255]
e = [0,0,0]
#creates image
image = [e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         r,b,b,b,b,b,b,r,
         r,b,b,b,b,b,b,r,
         r,b,b,b,b,b,b,r,
         r,b,b,b,b,b,b,r,
         r,b,b,b,b,b,b,r,
         r,r,r,r,r,r,r,r,]

sense.set_pixels(image) # this line assigns the image above to actually be displayed on the sensehat.

#Begins a While loop to retrieve orientation data and to set images dependent on roll
# orientation
while True:
    pitch, roll, yaw = sense.get_orientation_degrees().values() #sets variable for which values are retrieved
    print("pitch=%s, roll=%s, yaw=%s" % (pitch,roll,yaw)) #ensures that retrieved values are printed
    if roll <= 10 and roll >= 1: # sets roll conditions for which first image will be displayed

        image = [e,e,e,e,e,e,e,e,
                 b,e,e,e,e,e,e,e,
                 r,b,b,b,b,b,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)
    elif roll <= 16 and roll >= 10.1:

        image = [e,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,b,b,b,e,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)
    elif roll <= 22 and roll >= 16.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,b,b,b,e,e,r,
                 r,b,b,b,b,b,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)
    elif roll <= 28 and roll >= 22.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,b,b,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 35 and roll >= 28.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,b,b,e,r,
                 r,b,b,b,b,b,e,r,
                 r,b,b,b,b,b,b,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 40 and roll >= 35.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,b,e,e,e,e,r,
                 r,b,b,b,b,e,e,r,
                 r,b,b,b,b,b,e,r,
                 r,b,b,b,b,b,e,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 45 and roll >= 40.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,b,e,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,b,e,e,r,
                 r,b,b,b,b,b,e,r,
                 r,b,b,b,b,b,b,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 50 and roll >= 45.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,b,e,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,b,e,e,r,
                 r,b,b,b,b,e,e,r,
                 r,b,b,b,b,b,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 55 and roll >= 50.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,b,e,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,b,e,e,r,
                 r,b,b,b,b,b,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 60 and roll >= 55.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,b,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,b,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 65 and roll >= 60.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,e,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,b,b,b,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 69 and roll >= 65.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,e,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 75 and roll >= 69.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,e,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 77 and roll >= 75.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,e,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 78 and roll >= 77.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,e,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 79.5 and roll >= 78.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,b,e,e,e,e,r,
                 r,b,b,e,e,e,e,r,
                 r,b,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 80.6 and roll >= 79.6:

        image = [b,e,e,e,e,e,e,e,
                 b,b,b,e,e,e,e,e,
                 r,b,b,e,e,e,e,r,
                 r,b,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 81.9 and roll >= 80.6:

        image = [b,e,e,e,e,e,e,e,
                 b,b,b,e,e,e,e,e,
                 r,b,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 83 and roll >= 82:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,b,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 84 and roll >= 83.1:

        image = [b,e,e,e,e,e,e,e,
                 b,b,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 85 and roll >= 84.1:

        image = [e,e,e,e,e,e,e,e,
                 b,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    elif roll <= 86 and roll >= 85.1:

        image = [e,e,e,e,e,e,e,e,
                 e,e,e,e,e,e,e,e,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,e,e,e,e,e,e,r,
                 r,r,r,r,r,r,r,r,]

        sense.set_pixels(image)

    if roll >= 86.001 and roll <= 330: # These two lines end the loop after the roll value
                                       # is above or equal to 87.001. This is when all of the
                                       # should be poured out, and it ensures that when the
                                       # senseHAT is upright it does not dislay blue LEDs.
        break














