import cv2
import os

print(os.getcwd())
set_path = os.chdir('C:/Users/Naveed Ul Mustafa/OneDrive - Technische Universität Berlin/Germany Summer2021 (Done)/TU Berlin (Semester Docs+Course Work)/Summers 2023/cloned_repos/Computer-Vision-1-1/ex_3')
print(os.getcwd())

maxScaleUp = 100
scaleFactor = 1
scaleType = 0
maxType = 1

windowName = "Resize Image"
trackbarValue = "Scale"
trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"

# load an image
im = cv2.imread("../data/images/truth.png")

# Create a window to display results
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

# Callback functions
def scaleImage(*args):
    global scaleFactor
    global scaleType
    
    # Get the scale factor from the trackbar 
    if scaleType == 0:  # Scale Up
        scaleFactor = 1 + args[0]/100.0
    else:  # Scale Down
        scaleFactor = 1 - args[0]/100.0

    # Perform check if scaleFactor is zero
    if scaleFactor <= 0:
        scaleFactor = 0.1
    
    # Resize the image
    scaledImage = cv2.resize(im, None, fx=scaleFactor,\
            fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)

# Callback functions
def scaleTypeImage(*args):
    global scaleType
    global scaleFactor
    scaleType = args[0]
    scaleImage(scaleFactor * 100)  # recompute scaleFactor in scaleImage

cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, scaleImage)
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, scaleTypeImage)

cv2.imshow(windowName, im)
c = cv2.waitKey(0)

cv2.destroyAllWindows()