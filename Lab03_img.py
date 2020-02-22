# LABORATORIO N° 03
# WILLY FUENTES

#Sesión 3: Reconocimiento de patrones Introducción al reconocimiento de patrones.
#Librerías Pillow de procesamiento de imágenes con Python

# 1 Mostrar y grabar nueva imagen
import cv2
img = cv2.imread('image.jpg')

cv2.imshow('original.jpg', img)
cv2.imwrite('original.jpg', img)
cv2.waitkey(0)
cv2.destroyAllWindows()
