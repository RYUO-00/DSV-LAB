# Experiment 3c: Plotting multiple images in a grid
# Put 4 images (png/jpg/jpeg) inside a folder called 'images' next to this file,
# or change image_folder below. If the folder is missing, dummy images are used.
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image_folder = 'images'   # e.g. 'C:/Users/<name>/Desktop/images'
labels = ['coast', 'beach', 'building', 'city at night']

# ---------- Load images ----------
if os.path.isdir(image_folder):
    img_filenames = sorted(os.listdir(image_folder))
    # keep only image files
    img_filenames = [f for f in img_filenames
                     if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    imgs = [mpimg.imread(os.path.join(image_folder, name))
            for name in img_filenames[:4]]
else:
    print("Folder not found, using random dummy images")
    rng = np.random.default_rng(0)
    imgs = [rng.random((100, 100, 3)) for _ in range(4)]

# ---------- Create 2x2 grid ----------
fig, axes = plt.subplots(2, 2)
fig.set_size_inches(6, 6)
fig.dpi = 150
axes = axes.ravel()   # make the 2x2 array one-dimensional

# ---------- Plot images in the subplots ----------
for i in range(len(imgs)):
    axes[i].imshow(imgs[i])
    axes[i].set_xticks([])
    axes[i].set_yticks([])
    axes[i].set_xlabel(labels[i])

plt.tight_layout()
plt.show()
