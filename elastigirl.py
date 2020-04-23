from cloud import generate_cloud
import matplotlib.pyplot as plt

plt.imshow(generate_cloud(("Elastigirl", "Helen"), "images/Elastigirl.jpg"))
plt.savefig('wordclouds/elastigirl.jpg')
