#!/usr/bin/python3
"""
Module for serializing a Python dictionary to XML format and deserializing
XML back to a dictionary.

Functions:
    serialize_to_xml(dictionary, filename):
        Serializes a dictionary into XML and saves it to a file.

    deserialize_from_xml(filename):
        Reads an XML file and deserializes it into a Python dictionary.
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The target XML file path.

    Returns:
        None
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML content from a file into a Python dictionary.

    Args:
        filename (str): The XML file to read.

    Returns:
        dict: The deserialized dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    new_dict = {}
    for child in root:
        new_dict[child.tag] = child.text
    return new_dict
