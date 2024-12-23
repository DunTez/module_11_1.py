import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

image_path = f'./penguin.jpg'
image = Image.open(image_path)
image = image.resize((600, 850))
image.save(image_path)
arr = np.array([10, 20, 30, 40, 50])
result = arr + 10
print("Массив увеличенный на 10:", result)
x = np.linspace(0, 20, 100)
y = np.sin(x)
plt.figure(figsize=(6, 6))
plt.plot(x, y, 'b--', label='Sine curve')
plt.title('Plot of Sine Function')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.show()
