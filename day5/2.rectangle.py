import cv2
import matplotlib.pyplot as plt
img = cv2.imread("tower.jpg")
print(img.shape)


rec = cv2.rectangle(img,(20,40),(100,80),(0,0,105),3)
plt.imshow(cv2.cvtColor(rec,cv2.COLOR_BGR2RGB))
plt.show()