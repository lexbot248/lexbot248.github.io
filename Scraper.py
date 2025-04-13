import requests
from bs4 import BeautifulSoup

def get_headlines_from_url(url, source_name):
    print(f"Scraping {url}...")
    # prints the URL being scraped
    headlines = []
    # Empty list is created to store headlines from scraped websites

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        if "businesstoday" in url:
            for tag in soup.find_all(['h2', 'h3']):
                text = tag.get_text(strip=True)
                #This gets the text content inside the HTML tags and strips any surrounding whitespace.
                if text and len(text.split()) > 3:
                    #eliminates any headlines less than 4 words
                    headlines.append(f"[Business Today] {text}")

        elif "livemint" in url:
            for tag in soup.select("h2.headline, h2.title, h2.listingPage_headline, div.listingPage h2, div.cardHolder h2"):
                text = tag.get_text(strip=True)
                if text and len(text.split()) > 3:
                    headlines.append(f"[LiveMint] {text}")


        elif "thehindu" in url:
            for tag in soup.find_all("a", href=True):
                # This looks for all <a> tags that contain the href attribute
                text = tag.get_text(strip=True)
                href = tag["href"]
                if text and "/business/" in href and len(text.split()) > 3:
                    headlines.append(f"[The Hindu] {text}")

        else:
            # Fallback for unknown headlines
            for tag in soup.find_all(['h2', 'h3']):
                text = tag.get_text(strip=True)
                if text and len(text.split()) > 3:
                    headlines.append(f"[{source_name}] {text}")

        return list(set(headlines))

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []
    # If there’s an error during the scraping process, the error is caught, and an empty list is returned.

def main():
    output_file = "headings_output.txt"
    all_headlines = []

    with open("urls.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]
        # Opens orls.txt, and enters each line into the urls list

    for url in urls:
        source_name = "Unknown Source"
        if "businesstoday" in url:
            source_name = "Business Today"
        elif "livemint" in url:
            source_name = "LiveMint"
        elif "thehindu" in url:
            source_name = "The Hindu"

        headlines = get_headlines_from_url(url, source_name)
        all_headlines.extend(headlines)
        # Calls get_headlines_from_url to scrape headlines and insert them into all_headlines

    with open(output_file, "w", encoding="utf-8") as f:
        for headline in all_headlines:
            f.write(headline + "\n")
            # Outputs all headlines into output_file, one headline per line

    print(f"\n✅ Scraping complete. {len(all_headlines)} headlines saved to {output_file}.")
    #print completion

if __name__ == "__main__":
    main()
    # terminate program
