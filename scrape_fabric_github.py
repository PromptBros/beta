import requests
import json

# Function to scrape content from a raw GitHub URL
def scrape_system_md(url, pattern_name, section_headers):
    response = requests.get(url)
    content = response.text

    # Dictionary to store the scraped sections
    sections = {header: 'Not Found' for header in section_headers}

    # Splitting the content into lines
    lines = content.splitlines()

    current_section = None

    # Loop through each line to find relevant sections
    for line in lines:
        # Identify the section headings based on provided headers
        if line.strip() in [f"# {header}" for header in section_headers]:
            current_section = line.strip().replace("# ", "")
        elif line.startswith("#") and current_section:  # Stop after the last header is reached
            current_section = None
        elif current_section:
            # Accumulate content for the current section
            if sections[current_section] == 'Not Found':
                sections[current_section] = line + '\n'
            else:
                sections[current_section] += line + '\n'

    return {
        'title': pattern_name,
        'source': url,
        'content': sections
    }

# List of patterns to scrape, each with its respective URL and section headers
patterns_to_scrape = [
    {
        'pattern_name': 'create_academic_paper',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/create_academic_paper/system.md',
        'section_headers': ['IDENTITY AND PURPOSE', 'OUTPUT SECTIONS', 'OUTPUT INSTRUCTIONS']
    },
    {
        'pattern_name': 'analyze_interviewer_techniques',
        'url': 'https://raw.githubusercontent.com/danielmiessler/fabric/main/patterns/analyze_interviewer_techniques/system.md',
        'section_headers': ['IDENTITY', 'GOAL', 'STEPS']
    }
]

# List to store all scraped data
all_scraped_data = []

# Scrape each pattern
for pattern in patterns_to_scrape:
    scraped_content = scrape_system_md(
        url=pattern['url'],
        pattern_name=pattern['pattern_name'],
        section_headers=pattern['section_headers']
    )
    all_scraped_data.append(scraped_content)

# Save the combined output to a JSON file
output_filename = 'scraped_fabric_patterns.json'
with open(output_filename, 'w') as json_file:
    json.dump(all_scraped_data, json_file, indent=4)

print(f"Data has been scraped and saved to '{output_filename}'")
