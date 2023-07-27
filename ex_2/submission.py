# Import module
import cv2
import math
import os
print(os.getcwd())
set_path = os.chdir('C:/Users/Naveed Ul Mustafa/OneDrive - Technische Universität Berlin/Germany Summer2021 (Done)/TU Berlin (Semester Docs+Course Work)/Summers 2023/cloned_repos/Computer-Vision-1-1/ex_2')
print(os.getcwd())

# List to store x,y coordinates
top_left = []
bottom_right = []

# How the function is working?
# press a left mouse button at start (upper left) and stretch diagonaly on the anticipated rectangel (bottonm right)
# upon pressing "c", it cleares the draw and "esc" to exit

def draw_rectangle(action,x,y,flags,param):
    # Referencing global variables
    global top_left, bottom_right

    # Action to be taken when left mouse button is pressed
    if action==cv2.EVENT_LBUTTONDOWN:
        top_left=[(x,y)]
        # Mark the vertex
        cv2.rectangle(img, top_left[0], 1, (255,255,0), 2, cv2.LINE_AA)
    
    # Action to be taken when left mouse button is released
    elif action==cv2.EVENT_LBUTTONUP:
        bottom_right=[(x,y)]
        # Mark the vertex
        cv2.rectangle(img, top_left[0], bottom_right[0], (255,255,0), 2, cv2.LINE_AA)    # cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
        print(top_left, bottom_right)
        cv2.imshow('image',img)

# load an image
img = cv2.imread('boy.jpg',1)     
if img is None:
    print('Image could not be opened.')
    exit() 

# Make a temporary image, will be useful to clear the drawing
temp = img.copy()

cv2.namedWindow('image')

# highgui function called when mouse events occur
cv2.setMouseCallback('image',draw_rectangle)

# loop until escape character is pressed or mark == 2
k = 0

while k!=27 :
        
        cv2.imshow('image',img)
        cv2.putText(img, 'Press "c" to clear the image', (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
        k = cv2.waitKey(20) & 0xFF 

        # Another way of cloning
        if k==99:
            img = temp.copy()

cv2.destroyAllWindows()


