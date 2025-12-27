# -------------------------------------------------
# INTERMEDIATE WEB SCRAPER USING BEAUTIFUL SOUP
# Scrapes book data from multiple pages and saves
# it into a CSV file
# -------------------------------------------------

# Import required libraries
import requests                     # To send HTTP requests
from bs4 import BeautifulSoup       # To parse HTML content
import csv                          # To save data into CSV format

# Base URL of the website (demo scraping site)
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

# List to store all scraped book data
all_books = []

# Loop through first 3 pages (can increase if needed)
for page in range(1, 4):

    # Format URL for current page
    url = base_url.format(page)

    # Send request to website
    response = requests.get(url)

    # Check if request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page {page}")
        continue

    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers on the page
    books = soup.find_all("article", class_="product_pod")

    # Loop through each book container
    for book in books:

        # Extract book title
        title = book.h3.a["title"]

        # Extract price
        price = book.find("p", class_="price_color").text

        # Extract availability status
        availability = book.find("p", class_="instock availability").text.strip()

        # Store data as a dictionary
        book_data = {
            "Title": title,
            "Price": price,
            "Availability": availability
        }

        # Add dictionary to list
        all_books.append(book_data)

# -----------------------------------------
# Save scraped data into a CSV file
# -----------------------------------------

# Open CSV file in write mode
with open("books_data.csv", "w", newline="", encoding="utf-8") as file:

    # Define column headers
    fieldnames = ["Title", "Price", "Availability"]

    # Create CSV writer
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write header row
    writer.writeheader()

    # Write book data rows
    writer.writerows(all_books)

print("Scraping completed successfully!")
print("Data saved to books_data.csv")
