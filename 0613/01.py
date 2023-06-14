import cv2
import matplotlib.pyplot as plt

image = cv2.imread(('./data/image01.png'))
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)

