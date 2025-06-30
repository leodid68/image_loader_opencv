import argparse  # Importe le module argparse pour gérer les arguments en ligne de commande
import cv2  # Importe la bibliothèque OpenCV pour le traitement d'images

ap = argparse.ArgumentParser()  # Crée un objet ArgumentParser pour gérer les arguments de ligne de commande
ap.add_argument("-i", "--image", required=True, help="Path to the image")  # Ajoute un argument obligatoire pour spécifier le chemin de l'image
args = vars(ap.parse_args())  # Parse les arguments et les convertit en dictionnaire pour un accès facile

image = cv2.imread(args["image"])  # Charge l'image à partir du chemin spécifié dans les arguments
(h, w) = image.shape[:2]  # Récupère la hauteur (h) et la largeur (w) de l'image en utilisant la propriété shape
cv2.imshow("Original", image)  # Affiche l'image originale dans une fenêtre intitulée "Original"

(b, g, r) = image[0, 0]  # Récupère les valeurs BGR du pixel en position (0, 0) - coin supérieur gauche
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))  # Affiche les valeurs RGB du pixel (0, 0)

(b, g, r) = image[50, 50]  # Récupère les valeurs BGR du pixel en position (50, 50)
print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r, g, b))  # Affiche les valeurs RGB du pixel (50, 50)

# update pixel at 120, 120
image[120, 120] = (0, 0, 255)  # Modifie le pixel en position (120, 120) avec la couleur rouge (BGR: 0, 0, 255)
(b, g, r) = image[120, 120]  # Récupère les valeurs BGR du pixel modifié pour vérification
print("Pixel at (120, 120) - Red: {}, Green: {}, Blue: {}".format(r, g, b))  # Affiche les valeurs RGB du pixel modifié

cv2.imshow("Updated", image)  # Affiche l'image mise à jour dans une nouvelle fenêtre intitulée "Updated"
cv2.waitKey(0)  # Attend qu'une touche soit pressée avant de continuer (0 signifie attente indéfinie)

(cX, cY) = (w // 2, h // 2)  # Calcule les coordonnées du centre de l'image en divisant la largeur et la hauteur par 2