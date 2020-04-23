from cloud import generate_cloud
import matplotlib.pyplot as plt

plt.imshow(generate_cloud(("Mr. Incredible", "Bob"), "images/MrIncredible.jpg"))
plt.savefig('wordclouds/mr_incredible.jpg')
