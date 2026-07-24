import argparse
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

read = argparse.ArgumentParser()

read.add_argument("filename")

read.add_argument("--no_grid", action="store_false")

args = read.parse_args()

tree = ET.parse(args.filename)
root = tree.getroot()

x = []
y = []

for value in root.find("xdata"):
    x.append(float(value.text))
for value in root.find("ydata"):
    y.append(float(value.text))

plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.title("y=f(x)")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(args.no_grid)

plt.show()