import requests
from bs4 import BeautifulSoup

def get_headlines_from_url(url, source_name):
    print(f"Scraping {url}...")
    headlines = []

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        if "businesstoday" in url:
            # Business Today uses h2 or h3 without specific class
            for tag in soup.find_all(['h2', 'h3']):
                text = tag.get_text(strip=True)
                if text and len(text.split()) > 3:
                    headlines.append(f"[Business Today] {text}")

        elif "livemint" in url:
            for tag in soup.select("h2.headline, h2.title, h2.listingPage_headline, div.listingPage h2, div.cardHolder h2"):
                text = tag.get_text(strip=True)
                if text:
                    headlines.append(f"[LiveMint] {text}")


        elif "thehindu" in url:
            for tag in soup.find_all("a", href=True):
                text = tag.get_text(strip=True)
                href = tag["href"]
                if text and "/business/" in href and len(text.split()) > 3:
                    headlines.append(f"[The Hindu] {text}")

        else:
            # Generic fallback
            for tag in soup.find_all(['h2', 'h3']):
                text = tag.get_text(strip=True)
                if text and len(text.split()) > 3:
                    headlines.append(f"[{source_name}] {text}")

        return list(set(headlines))  # Deduplicate

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

def main():
    output_file = "headings_output.txt"
    all_headlines = []

    with open("urls.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]

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

    with open(output_file, "w", encoding="utf-8") as f:
        for headline in all_headlines:
            f.write(headline + "\n")

    print(f"\n✅ Scraping complete. {len(all_headlines)} headlines saved to {output_file}.")

if __name__ == "__main__":
    main()
