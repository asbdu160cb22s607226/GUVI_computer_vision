import cv2
import matplotlib.pyplot as plt
img = cv2.imread("nature beauty.jpg")
print(img.shape)
rec=cv2.rectangle(img,(50,50),(200,100),(255,0,0),2)
plt.imshow( cv2.cvtColor(rec,cv2.COLOR_BGR2RGB))
plt.show()