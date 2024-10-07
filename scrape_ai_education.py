import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_prompts(urls):
    prompts_data = []

    for url in urls:
        try:
            print(f"Scraping: {url}")
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract the title
            title_tag = soup.find('h1')
            title = title_tag.text.strip() if title_tag else "No title found"

            # Extract the example prompt
            example_prompt_tag = soup.find('strong', text='Example Prompt')
            if example_prompt_tag:
                # Get the parent of the example prompt, then find the next sibling
                prompt = example_prompt_tag.find_next('p').text.strip() if example_prompt_tag.find_next('p') else "No prompt found"
            else:
                prompt = "No prompt found"

            # Append the data to the list
            prompts_data.append({
                "title": title,
                "prompt": prompt,
                "source": url
            })

            # Sleep to avoid overwhelming the server
            time.sleep(1)

        except Exception as e:
            print(f"Error while scraping {url}: {e}")

    return prompts_data

# List of URLs to scrape (Thanksgiving activities URL removed)
urls = [
    "https://www.aiforeducation.io/prompts/critically-analyze-ai-outputs-using-an-ai-chatbot",
    "https://www.aiforeducation.io/prompts/smart-goal-generation",
    "https://www.aiforeducation.io/prompts/break-down-goals-into-objectives",
    "https://www.aiforeducation.io/prompts/ell-instructions-translator",
    "https://www.aiforeducation.io/prompts/language-learning-practice-partner",
    "https://www.aiforeducation.io/prompts/research-project-ideas",
    "https://www.aiforeducation.io/prompts/explain-it-to-me-like",
    "https://www.aiforeducation.io/prompts/studying-help",
    "https://www.aiforeducation.io/prompts/flashcards",
    "https://www.aiforeducation.io/prompts/college-essay-ideas",
    "https://www.aiforeducation.io/prompts/summarize-text",
    "https://www.aiforeducation.io/prompts/time-travel",
    "https://www.aiforeducation.io/prompts/emoji-translator",
    "https://www.aiforeducation.io/prompts/celebrity-heads-game",
    "https://www.aiforeducation.io/prompts/model-un-model-congress"
]

# Run the scraping function
prompts = scrape_prompts(urls)

# Write the scraped data to a JSON file
with open('prompts_ai_education.json', 'w') as f:
    json.dump(prompts, f, indent=4)

print("Scraping completed successfully.")
