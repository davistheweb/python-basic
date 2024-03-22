import requests

def fetch_book_info(book_id):
    # URL of the API endpoint to retrieve book information
    url = f"https://example.com/api/books/{book_id}"

    try:
        # Sending a GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extracting JSON data from the response
            book_info = response.json()
            return book_info
        else:
            print(f"Failed to fetch book info. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error fetching book info: {e}")
        return None

# Example usage
book_id = 123  # Replace with the ID of the book you want to retrieve
book_info = fetch_book_info(book_id)
if book_info:
    print("Book Information:")
    print(f"Title: {book_info['title']}")
    print(f"Author: {book_info['author']}")
    print(f"Published Date: {book_info['published_date']}")
    # Add more fields as needed
else:
    print("Failed to fetch book information.")
