
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

folder = 'C:\\Users\\ADMIN\\Desktop\\dsv_programs\\images'
labels = ['coast', 'beach', 'building', 'city at night']


files = sorted(os.listdir(folder))[:4]
imgs = [ mpimg.imread(os.path.join(folder, f)) for f in files ]


fig, axes = plt.subplots(2, 2, figsize=(6, 6), dpi=150)

for ax, img, label in zip(axes.ravel(), imgs, labels):
    ax.imshow(img)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(label)

plt.tight_layout()
plt.show()
