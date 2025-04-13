# News Headline Web Scraper

This Python project scrapes the latest business news headlines from major Indian news websites and saves them to a local text file.

# Supported Sources
- [Business Today](https://www.businesstoday.in/)
- [LiveMint](https://www.livemint.com/)
- [The Hindu - Business Section](https://www.thehindu.com/business/)

# Features
- Automatically detects which website is being scraped.
- Extracts headlines based on each site's HTML structure.
- Filters out short or all-uppercase non-headlines.
- Saves all collected headlines in a clean, readable format to `headings_output.txt`.

# Set-up
Make sure you have miniconda installed
Then run:
conda env create -f requirements.yml
conda activate webscraper

# Usage
- Add the URLs you want to use in urls.txt, one per line. Example:
https://www.businesstoday.in/latest/in-focus
https://www.livemint.com/news/india
https://www.thehindu.com/business/

Run the scraper
- python scraper.py

Scraped headlines will be saved in headings_output.txt

# Example output
[Business Today] Ferrari unveils $423,000 sports car for traditional v12 lovers ahead of Miami Grand Prix
[LiveMint] India’s semiconductor demand to see 15% CAGR, hit $108 billion by 2030
[The Hindu] Ola Electric rolls out Roadster X bike from Tamil Nadu plant