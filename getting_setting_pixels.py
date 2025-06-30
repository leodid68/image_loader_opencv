import argparse  # Importe le module argparse pour gérer les arguments en ligne de commande
import cv2  # Importe la bibliothèque OpenCV pour le traitement d'images
import numpy as np

ap = argparse.ArgumentParser()  # Crée un objet ArgumentParser pour gérer les arguments
ap.add_argument("-i", "--image", required=True, help="Path to the image")  # Ajoute un argument obligatoire pour spécifier le chemin de l'image
args = vars(ap.parse_args())  # Parse les arguments et les convertit en dictionnaire

image = cv2.imread(args["image"])  # Charge l'image à partir du chemin spécifié

(h, w) = image.shape[:2]  # Récupère la hauteur (h) et la largeur (w) de l'image
print("Width: {} pixels, Height: {}".format(w, h))

cv2.imshow("Original", image)  # Affiche l'image originale dans une fenêtre

(b, g, r) = image[0, 0]  # Récupère les valeurs BGR du pixel en position (0, 0)
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))  # Affiche les valeurs RGB du pixel (0, 0)

(b, g, r) = image[640, 505]  # Récupère les valeurs BGR du pixel en position (640, 505)
print("Pixel at (640, 505) - Red: {}, Green: {}, Blue: {}".format(r, g, b))  # Affiche les valeurs RGB du pixel (640, 505)

# update pixel at 640, 505
image[640, 505] = (0, 0, 255)  # Modifie le pixel en position (640, 505) avec la couleur rouge (BGR: 0, 0, 255)
(b, g, r) = image[640, 505]  # Récupère les valeurs BGR du pixel modifié
print("Pixel at (640, 505) - Red: {}, Green: {}, Blue: {}".format(r, g, b))  # Affiche les valeurs RGB du pixel modifié

(b, g, r) = image[360, 720]
print("Pixel at (360, 720) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

(cX, cY) = (w // 2, h // 2)  # Calcule les coordonnées du centre de l'image
print("Center of the image - X: {}, Y: {}".format(cX, cY)) # cX est la largeur de l'image // 2 et cY est la hauteur de l'image // 2

cv2.imshow("Updated", image)  # Affiche l'image mise à jour dans une nouvelle fenêtre
cv2.waitKey(0)  # Attend qu'une touche soit pressée pour continuer

# Extrait le quart supérieur gauche de l'image (du point 0,0 jusqu'au centre)
top_left = image[0:cY, 0:cX]
# Affiche le quart supérieur gauche dans une fenêtre intitulée "Top Left"
cv2.imshow("Top Left", top_left)
# Attend qu'une touche soit pressée pour continuer
cv2.waitKey(0)

# Extrait le quart supérieur droit de l'image (de la moitié de la largeur jusqu'à la largeur totale, et du haut jusqu'à la moitié de la hauteur)
top_right = image[0:cY, cX:w]
# Affiche le quart supérieur droit dans une fenêtre intitulée "Top Right"
cv2.imshow("Top Right", top_right)
# Attend qu'une touche soit pressée pour continuer
cv2.waitKey(0)

# Extrait le quart inférieur droit de l'image (de la moitié de la hauteur jusqu'à la hauteur totale, et de la moitié de la largeur jusqu'à la largeur totale)
bottom_right = image[cY:h, cX:w]
# Affiche le quart inférieur droit dans une fenêtre intitulée "Bottom Right"
cv2.imshow("Bottom Right", bottom_right)
# Attend qu'une touche soit pressée pour continuer
cv2.waitKey(0)

# Extrait le quart inférieur gauche de l'image (de la moitié de la hauteur jusqu'à la hauteur totale, et du début jusqu'à la moitié de la largeur)
bottom_left = image[cY:h, 0:cX]
# Affiche le quart inférieur gauche dans une fenêtre intitulée "Bottom Left"
cv2.imshow("Bottom Left", bottom_left)
# Attend qu'une touche soit pressée pour continuer
cv2.waitKey(0)

# Colorie le quart supérieur gauche de l'image en bleu (format BGR: 255,0,0)
image[0:cY, 0:cX] = (255, 0, 0)
# Affiche l'image modifiée avec le carré bleu dans une fenêtre intitulée "Carré bleu"
cv2.imshow("Carré bleu", image)
# Attend qu'une touche soit pressée pour continuer
cv2.waitKey(0)