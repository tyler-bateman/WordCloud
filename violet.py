from cloud import generate_cloud
import matplotlib.pyplot as plt

plt.imshow(generate_cloud(("Violet",), "images/Violet.jpg"))
plt.savefig("wordclouds/violet.jpg")
