import requests

def check_website_status(url):
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        if status_code == 200:
            print(f"Website {url} is live and active.")
        else:
            print(f"Website {url} returned status code: {status_code}.")
        return status_code
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None

def main():
    # Replace with the website you want to monitor
    website_url = "https://example.com"
    status = check_website_status(website_url)
    if status is None:
        print("Website is not reachable or there was an error.")

if __name__ == "__main__":
    main()
