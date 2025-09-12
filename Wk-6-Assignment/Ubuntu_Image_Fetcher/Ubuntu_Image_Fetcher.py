import requests
import os
from urllib.parse import urlparse
from hashlib import md5

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:
        filename = f"image_{md5(url.encode()).hexdigest()[:8]}.jpg"
    return filename

def is_duplicate(filepath, content):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            existing = f.read()
        return existing == content
    return False

def fetch_and_save_image(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Check headers
        content_type = response.headers.get('Content-Type', '')
        if not content_type.startswith('image/'):
            print(f"✗ Skipped: URL does not point to an image ({content_type})")
            return

        filename = get_filename_from_url(url)
        filepath = os.path.join("Fetched_Images", filename)

        if is_duplicate(filepath, response.content):
            print(f"⚠️ Duplicate detected: {filename} already exists.")
            return

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    os.makedirs("Fetched_Images", exist_ok=True)

    urls = input("Enter image URLs separated by commas:\n").split(',')

    for url in map(str.strip, urls):
        if url:
            fetch_and_save_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
