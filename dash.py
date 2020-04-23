from cloud import generate_cloud
import matplotlib.pyplot as plt

plt.imshow(generate_cloud(("Dash",), "images/Dash.jpg"))
plt.savefig("wordclouds/dash.jpg")
