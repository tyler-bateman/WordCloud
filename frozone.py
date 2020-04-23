from cloud import generate_cloud
import matplotlib.pyplot as plt

plt.imshow(generate_cloud(("Frozone", "Lucius"), "images/Frozone.jpeg"))
plt.savefig("wordclouds/frozone.jpg")
