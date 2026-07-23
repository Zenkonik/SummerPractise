import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET


xmin = -100
xmax = 100
count = 500
x = np.linspace(xmin, xmax, count)
y = -np.cos(x) * np.cos(np.pi) * np.exp(-((x - np.pi)**2))

plt.plot(x, y)
plt.show()

root = ET.Element("data")
xdata = ET.SubElement(root, "xdata")
for value in x:
    elem = ET.SubElement(xdata, "x")
    elem.text = f"{value:.2f}"

ydata = ET.SubElement(root, "ydata")
for value in y:
    elem = ET.SubElement(ydata, "y")
    elem.text = f"{value:.2f}"
tree = ET.ElementTree(root)
ET.indent(tree, space="    ", level=0)
tree.write("results.xml", encoding="utf-8", xml_declaration=True)