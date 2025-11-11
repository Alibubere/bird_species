import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

base_dir = "data\images"

# List categories
categories = os.listdir(base_dir)
print(f"Number of species: {len(categories)}")
print("Example species:", categories[:5])

# View random images
random_species = random.choice(categories)
species_path = os.path.join(base_dir, random_species)
sample_images = os.listdir(species_path)[:5]

plt.figure(figsize=(15, 5))
for i, img_name in enumerate(sample_images):
    img_path = os.path.join(species_path, img_name)
    img = mpimg.imread(img_path)
    plt.subplot(1, 5, i+1)
    plt.imshow(img)
    plt.title(random_species)
    plt.axis("off")
plt.show()

count = sum([len(files) for _, _, files in os.walk(base_dir)])
print(f"Total training images: {count}")
