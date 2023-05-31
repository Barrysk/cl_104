import cv2

# Leer la imagen
img = cv2.imread("solar-system.jpg")

# Agregar texto debajo de cada planeta con tamaño de fuente reducido
font_scale = 0.5

cv2.putText(img, "Mercurio", (120, 250), cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 255), 2)
cv2.putText(img, "Venus", (190, 260), cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 255), 2)
cv2.putText(img, "Tierra", (290, 260), cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 255), 2)
cv2.putText(img, "Marte", (380, 260), cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 255), 2)
cv2.putText(img, "Júpiter", (580, 390), cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 255), 2)
cv2.putText(img, "Saturno", (760, 310), cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 255), 2)
cv2.putText(img, "Urano", (975, 290), cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 255), 2)
cv2.putText(img, "Neptuno", (1115, 290), cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 255), 2)

# Mostrar la imagen
cv2.imshow("Resultado", img)

# Esperar hasta que se presione una tecla
cv2.waitKey(0)

# Guardar la imagen final
cv2.imwrite("Sistema_solar_con_nombres.jpg", img)
