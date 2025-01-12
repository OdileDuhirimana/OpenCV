import cv2

image = cv2.imread("assignment-001-given.jpg")
overlay = image.copy()
cv2.rectangle(overlay, (790, 75), (1250, 170), (0, 0, 0), -1)
cv2.addWeighted(overlay, 0.7, image, 0.3, 0, image)
cv2.putText(image, "RAH974U", (800, 150), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 4)
cv2.rectangle(image, (260, 180), (1000, 950), (0, 255, 0), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
