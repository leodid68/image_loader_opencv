import argparse
import cv2

# opencv-load-image python load_images.py -i image.jpg

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--test", required=True, help="Path to the image")
args = vars(ap.parse_args()) # vars() converts the dictionary to a dictionary

van_gogh = cv2.imread(args["test"])
(h, w, c) = van_gogh.shape[:3] # Height, width, channels, [:3] means all

print("width: {}, height: {}, channels: {}".format(w, h, c))

cv2.imshow("image", van_gogh) #"image" is the window name, image is the image object
cv2.waitKey(0)

cv2.imwrite("new_image.jpg", van_gogh)