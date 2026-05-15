import xml.etree.ElementTree as ET
import re

ET.register_namespace('', 'http://www.w3.org/2000/svg')
tree = ET.parse('logoo.svg')
root = tree.getroot()

# Let's just adjust the HTML instead using a container with hidden overflow and negative margins,
# or we can remove the empty space using CSS scale.
