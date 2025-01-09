

from urllib.parse import urlparse
from bs4 import BeautifulSoup


def is_phishing(url):
    try:
       
        domain = urlparse(url).netloc

       
        phishing_domains = ["bit.ly", "tinyurl.com", "goo.gl"]
        for phishing_domain in phishing_domains:
            if phishing_domain in domain:
                return True

       
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

       
        suspicious_keywords = ["login", "password", "username", "email", "credit card"]
        for keyword in suspicious_keywords:
            if keyword in soup.text.lower():
                return True

       
        return False

    except Exception as e:
        print(f"Error checking URL: {e}")
        return False


def main():
    url = input("Enter URL to check: ")
    if is_phishing(url):
        print("This might be a phishing site!")
    else:
        print("This seems safe.")

if __name__ == "__main__":
    main()
