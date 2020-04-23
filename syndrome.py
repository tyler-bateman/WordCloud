from cloud import generate_cloud
import matplotlib.pyplot as plt

plt.imshow(generate_cloud(("Buddy", "Incrediboy", "Syndrome"), "images/Syndrome.jpeg"))
plt.savefig("wordclouds/syndrome.jpg")
