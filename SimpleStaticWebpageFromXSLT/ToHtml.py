from lxml import etree


def transform_xml_with_xslt(xml_file_path, xslt_file_path, output_html_path):
    # Parse the XML and XSLT files
    xml_tree = etree.parse(xml_file_path)
    xslt_tree = etree.parse(xslt_file_path)

    # Create an XSLT transformer
    transform = etree.XSLT(xslt_tree)

    # Apply the transformation
    transformed_tree = transform(xml_tree)

    # Save the transformed HTML to a file
    with open(output_html_path, 'wb') as output_file:
        output_file.write(etree.tostring(transformed_tree, pretty_print=True, method="html"))



