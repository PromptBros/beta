import requests
import xml.etree.ElementTree as ET
import os

# We would like to acknowledge and thank that the caselaw national archives team opened up this data set.
# Freely distributed under https://caselaw.nationalarchives.gov.uk/open-justice-licence

# This scraper was built with help of PromptBros.ai
# built with help of PromptBros.ai - https://promptbros.ai/agent/clxrrl4ek0001vj3q9vql7gel?chat=VSCp87NgXxT3qz5LjBfvuVxsN


def download_xml_file(url, folder_path):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.replace("https://caselaw.nationalarchives.gov.uk/", "").replace("/", "_")
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download: {url}")

def process_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    if response.status_code == 200:
        sitemap_content = response.text
        root = ET.fromstring(sitemap_content)
        
        for sitemap in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap")[2:]:
            loc = sitemap.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
            process_loc_file(loc)
    else:
        print(f"Failed to retrieve sitemap: {sitemap_url}")

def process_loc_file(loc_url):
    response = requests.get(loc_url)
    if response.status_code == 200:
        loc_content = response.text
        root = ET.fromstring(loc_content)
        
        folder_path = loc_url.replace("https://caselaw.nationalarchives.gov.uk/", "").replace(".xml", "")
        os.makedirs(folder_path, exist_ok=True)
        
        for url in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
            loc = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
            data_url = loc + "/data.xml"
            download_xml_file(data_url, folder_path)
    else:
        print(f"Failed to retrieve loc file: {loc_url}")

# Main execution
sitemap_url = "https://caselaw.nationalarchives.gov.uk/sitemap.xml"
process_sitemap(sitemap_url)