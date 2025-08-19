import cv2
import matplotlib.pyplot as plt
img = cv2.imread("bird.jpeg")
print(img.shape)

circle=cv2.circle(img,(50,50),50,(255,0,0),2)

plt.imshow( cv2.cvtColor(circle,cv2.COLOR_BGR2RGB))
plt.show()