import cv2
import numpy as np

rectangle = np.zeros(shape=(300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

circle = np.zeros(shape=(300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
cv2.waitKey(0)

# Résultat : intersection (zone commune rectangle + cercle)
# Si pixel rectangle = 255 ET pixel cercle = 255 → résultat = 255
# Sinon → résultat = 0
# AND masquage (garder les zones communes)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("And", bitwiseAnd)
cv2.waitKey(0)

# Résultat : union (rectangle + cercle combinés)
# Si pixel rectangle = 255 OU pixel cercle = 255 → résultat = 255
# Sinon → résultat = 0
# OR fusion image

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("Or", bitwiseOr)
cv2.waitKey(0)

# Résultat : différence symétrique (rectangle + cercle SANS intersection)
# Si pixel rectangle ≠ pixel cercle → résultat = 255
# Si pixel rectangle = pixel cercle → résultat = 0
# XOR detection des differences

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("Xor", bitwiseXor)
cv2.waitKey(0)

# Principe : Inverse tous les pixels
# Si pixel = 255 → résultat = 0
# Si pixel = 0 → résultat = 255

bitwiseNot = cv2.bitwise_not(rectangle)
cv2.imshow("Not", bitwiseNot)
cv2.waitKey(0)