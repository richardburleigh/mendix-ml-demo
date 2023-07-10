import requests
import markdown
import os
from urllib.parse import urlparse
import wikipediaapi

outdir = "./data"

def download_wikipedia_article(url):
    parsed_url = urlparse(url)
    article_id = parsed_url.path.split('/')[-1]

    # Create a Wikipedia API client with a custom user agent
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent='Mendix AI Demo'  # Replace with your own user agent string
    )


    # Fetch the page
    page = wiki_wiki.page(article_id)

    if page.exists():
        # Convert the page content to markdown
        markdown_content = markdown.markdown(page.text)

        # Save the markdown content to a file
        filename = f'{article_id}.html'
        with open(os.path.join(outdir,filename), 'w', encoding='utf-8') as file:
            file.write(markdown_content)
        
        print(f'Successfully downloaded {article_id} to {filename}')
    else:
        print(f'Article {article_id} does not exist.')


# List of Wikipedia article URLs to download
article_urls = [
    'https://en.wikipedia.org/wiki/Low-code_development_platform',
    'https://en.wikipedia.org/wiki/Siemens_Digital_Industries_Software',
    'https://en.wikipedia.org/wiki/Siemens',
    'https://en.wikipedia.org/wiki/Otter',
    'https://en.wikipedia.org/wiki/Alpaca',
    'https://en.wikipedia.org/wiki/Thailand',
    'https://en.wikipedia.org/wiki/Thai_cuisine'
]

# Create a directory to store the downloaded articles
output_dir = 'wikipedia_articles'
os.makedirs(output_dir, exist_ok=True)

# Download each article
for url in article_urls:
    download_wikipedia_article(url)

