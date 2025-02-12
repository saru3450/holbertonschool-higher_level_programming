#!/usr/bin/python3
"""
Serialization and deserialization using XML
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.
    """
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():

            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception as e:
        print(f"Error serializing to XML: {e}")


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except ET.ParseError:
        print(f"Error: Failed to parse the XML file '{filename}'.")
        return None
