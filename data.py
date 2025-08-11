import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

def scrape_products(url, output_file='products.csv'):
    """
    Scrapes product information from an e-commerce website and saves to CSV
    :param url: URL of the e-commerce category/page to scrape
    :param output_file: Name of the output CSV file
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Fetch the webpage
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Initialize list to store product data
        products = []
        
        # Extract product information
        # Note: These selectors need to be customized for the specific website
        product_cards = soup.select('div.product-card')  # Update this selector
        
        for card in product_cards:
            try:
                name = card.select_one('h2.product-title').text.strip()
                price = card.select_one('span.price').text.strip()
                rating = card.select_one('div.rating').text.strip() if card.select_one('div.rating') else 'N/A'
                
                # Get absolute URL for product link if needed
                product_url = card.find('a')['href']
                product_url = urljoin(url, product_url)
                
                products.append({
                    'name': name,
                    'price': price,
                    'rating': rating,
                    'url': product_url
                })
            except Exception as e:
                print(f"Error extracting product: {e}")
                continue
        
        # Save to CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'price', 'rating', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for product in products:
                writer.writerow(product)
        
        print(f"Successfully scraped {len(products)} products. Data saved to {output_file}")
        
    except Exception as e:
        print(f"Error during scraping: {e}")

# Example usage
if __name__ == "__main__":
    print("E-commerce Product Scraper")
    print("==========================")
    
    website_url = input("Enter the URL of the e-commerce category page to scrape: ")
    output_filename = input("Enter output CSV filename (default: products.csv): ") or "products.csv"
    
    scrape_products(website_url, output_filename)
