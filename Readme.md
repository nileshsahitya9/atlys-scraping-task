# Scraper App

This project is a web scraping tool built using Python and the FastAPI framework. The tool scrapes product information from a given website and stores the data locally. It includes features such as pagination, proxy usage, retry mechanisms, caching, and simple authentication.

## Features

- Scrape product name, price, and image from a specified number of pages.
- Option to use a proxy for scraping.
- Simple authentication using a static token.
- Retry mechanism for handling server errors.
- Caching of scraped results to avoid unnecessary updates.
- Storing scraped data in a local JSON file.
- Notification of the scraping status.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/scraper_app.git
    cd scraper_app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

2. Access the FastAPI documentation at `http://127.0.0.1:8000/docs`.

3. Use the `/scrape/` endpoint to start scraping. You can provide optional parameters for the number of pages and proxy:
    ```http
    POST /scrape/?limit=5&proxy=http://yourproxy:port
    ```

    Include the `Authorization` header with the static token:
    ```http
    Authorization: your_static_token_here
    ```

## Configuration

- **Static Token**: Set your static token in the `auth.py` file.
- **Base URL**: Change the base URL for scraping in the `scraper.py` file if needed.
- **Local JSON Storage**: The scraped data is stored in `products.json`.

## Project Structure

/scraper_app
│
├── main.py # FastAPI application
├── models.py # Data models
├── cache.py # caching
├── scraper.py # Scraping logic
├── storage.py # Storage logic (e.g., JSON storage)
├── notifications.py # Notification logic
├── auth.py # Authentication logic
├── requirements.txt # Project dependencies
└── README.md # Documentation


## Dependencies

- FastAPI
- Uvicorn
- Requests
- BeautifulSoup4
- Pydantic
- Redis

