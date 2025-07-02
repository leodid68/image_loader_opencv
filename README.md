# Image Loader & Processor avec OpenCV

Ce projet est une collection de notebooks Jupyter et de scripts Python qui démontrent l'utilisation d'OpenCV pour le chargement, la manipulation et le traitement d'images.

## Structure du projet

Le projet est organisé en plusieurs modules avec leurs notebooks correspondants :

### 📁 Notebooks principaux
- **`resizing_image.ipynb`** : Redimensionnement d'images avec différentes méthodes d'interpolation
- **`translate_opencv.ipynb`** : Translation/déplacement d'images
- **`rotation_opencv.ipynb`** : Rotation d'images avec différents angles
- **`drawing_opencv.ipynb`** : Dessin de formes géométriques sur images
- **`opencv_flip.ipynb`** : Retournement d'images (horizontal, vertical, diagonal)

### 📁 Scripts Python
- **`load_images.py`** : Script en ligne de commande pour charger et analyser des images
- **`getting_setting_pixels.py`** : Manipulation des pixels individuels

### 📁 Dossiers de sortie
- **`getting_setting_pixels/`** : Résultats de manipulation des pixels
- **`translate_open_cv_image/`** : Images traduites/déplacées
- **`resizing_image/`** : Images redimensionnées avec différentes méthodes
- **`drawing_opencv/`** : Images avec dessins et formes ajoutées
- **`open_cv_flip/`** : Images retournées
- **`load_images/`** : Images chargées et analysées

### 🖼️ Images de test
- **`Van_Gogh-Starry_Night.jpg`** : Image principale utilisée dans les exemples
- **`Saint_Joseph_charpentier.jpg`** : Image secondaire pour les tests

## Fonctionnalités principales

### 🔄 Redimensionnement d'images
- Comparaison de 5 méthodes d'interpolation :
  - `INTER_NEAREST` : Plus rapide, effet pixelisé
  - `INTER_LINEAR` : Bon compromis qualité/vitesse
  - `INTER_AREA` : Optimal pour réduction d'images
  - `INTER_CUBIC` : Meilleure qualité pour agrandissement
  - `INTER_LANCZOS4` : Qualité supérieure, plus lent

### 🎨 Dessin et manipulation
- Dessin de lignes, rectangles et cercles
- Ajout de formes avec couleurs aléatoires
- Manipulation des pixels individuels
- Transformations géométriques

### 🔄 Transformations
- Translation avec matrices de transformation
- Rotation avec angles personnalisés
- Retournement (flip) horizontal/vertical
- Combinaison de transformations multiples

## Prérequis

- Python 3.12+
- OpenCV (`cv2`)
- NumPy
- imutils
- Matplotlib
- IPython/Jupyter
- Pillow (PIL)

## Installation