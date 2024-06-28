import requests
from bs4 import BeautifulSoup
import pandas as pd
import CsvToXml
import ToHtml
from CoordinateConverter import convert_csv_coordinates

# url to scrape
url = "https://en.wikipedia.org/wiki/List_of_Roman_villas_in_England"

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the relevant information from the HTML code

# Select all tables with the class 'wikitable'
tables = soup.select('#mw-content-text > div.mw-content-ltr.mw-parser-output > table.wikitable')

# Extract villa names, grid references, and links from all selected tables
data = []
for table in tables:
    for row in table.find_all('tr')[1:]:  # Skip the header row
        cells = row.find_all('td')
        if len(cells) >= 4:  # Ensure there are enough columns
            villa_name = cells[0].get_text(strip=True)
            wiki_link_text = cells[1].get_text(strip=True)
            wiki_link = cells[1].find('a')['href']
            grid_reference = cells[2].get_text(strip=True)
            link_tag = cells[3].find('a')
            link = link_tag['href'] if link_tag else 'N/A'
            wiki_link = str.replace(wiki_link, ',', '') if wiki_link else 'N/A'
            wiki_link = str.replace(wiki_link, '"', '') if wiki_link else 'N/A'
            wiki_link_text = str.replace(wiki_link_text, ',', '')
            wiki_link_text = str.replace(wiki_link_text, '"', '')
            data.append({'Villa Name': villa_name, 'Wiki Link Text': wiki_link_text, 'Wiki Link': wiki_link,
                         'Grid Reference': grid_reference, 'Link': link})

# Create a DataFrame
df = pd.DataFrame(data)

# Export to CSV
df.to_csv('roman_villas.csv', index=False)

print('CSV file has been created successfully.')

# Paths to the input and output CSV files
input_csv_path = 'roman_villas.csv'
output_csv_path = 'roman_villas_with_lat_lon.csv'

# Perform the conversion
convert_csv_coordinates(input_csv_path, output_csv_path)

print(f"Conversion complete. The output CSV has been saved to {output_csv_path}")

xml = CsvToXml.csv_to_xml(output_csv_path)

with open('roman_villas.xml', 'w') as file:
    file.write(xml)

# Paths to the XML, XSLT, and output HTML files
xml_file_path = 'roman_villas.xml'
xslt_file_path = 'ToSimpleHtml.xsl'
output_html_path = 'SimpleHtml.html'

# Perform the transformation and save the output
ToHtml.transform_xml_with_xslt(xml_file_path, xslt_file_path, output_html_path)

print(f"Transformation complete. The output HTML has been saved to {output_html_path}")
