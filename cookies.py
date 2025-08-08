import cloudscraper
from urllib.parse import urljoin, urlparse
import re
import sys

def extract_urls(html, base_url):
    # Regex to find href/src URLs
    urls = set()
    # href and src attributes
    pattern = re.compile(r'(?:href|src)="([^"#]+)"')
    for match in pattern.findall(html):
        # Make absolute URL
        full_url = urljoin(base_url, match)
        # Only keep URLs from the same domain or subdomains
        if urlparse(full_url).netloc.endswith(urlparse(base_url).netloc):
            urls.add(full_url)
    return urls

def main(target_url):
    scraper = cloudscraper.create_scraper()
    print(f"[+] Fetching {target_url} ...")
    response = scraper.get(target_url)
    if response.status_code != 200:
        print(f"[-] Failed to fetch page, status code: {response.status_code}")
        return

    html = response.text

    # Extract URLs
    urls = extract_urls(html, target_url)
    print(f"[+] Found {len(urls)} URLs")

    # Save full URLs to file
    with open("endpoints.txt", "w") as f:
        for url in sorted(urls):
            f.write(url + "\n")
    print("[+] Saved full URLs to endpoints.txt")

    # Save cookies to file
    cookies = scraper.cookies.get_dict()
    with open("cookies.txt", "w") as f:
        for k, v in cookies.items():
            f.write(f"{k}={v}\n")
    print("[+] Saved cookies to cookies.txt")

    # Save headers to file
    with open("headers.txt", "w") as f:
        for k, v in response.headers.items():
            f.write(f"{k}: {v}\n")
    print("[+] Saved headers to headers.txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} https://coinbase.com")
        sys.exit(1)
    main(sys.argv[1])
