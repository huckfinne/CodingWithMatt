import csv
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree


def csv_to_xml(csv_file_path):
    # Read the CSV data from the file
    with open(csv_file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)

        # Create the root element
        root = Element('rows')

        # Process each row in the CSV
        for row in csv_reader:
            location, area, wiki_link, coordinates, heritage_link, lat, lon = row

            # Create a row element
            row_elem = SubElement(root, 'row')

            # Add child elements to the row element
            SubElement(row_elem, 'location').text = location
            SubElement(row_elem, 'area').text = area
            SubElement(row_elem, 'wiki_link').text = wiki_link
            SubElement(row_elem, 'coordinates').text = coordinates
            SubElement(row_elem, 'heritage_link').text = heritage_link

            if lat is not None and lon is not None:
                SubElement(row_elem, 'latitude').text = str(lat)
                SubElement(row_elem, 'longitude').text = str(lon)

    # Create an ElementTree object from the root element
    tree = ElementTree(root)

    # Return the XML string
    return tostring(root, encoding='unicode')

