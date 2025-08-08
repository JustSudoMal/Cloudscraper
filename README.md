This Python script is a lightweight web recon tool using cloudscraper to bypass bot protection, crawl a page, and extract useful target info.
🔍 What It Does

Given a URL, it:

    Fetches the HTML using cloudscraper (bypasses Cloudflare anti-bot).

    Extracts all internal URLs from href and src attributes.

    Saves:

        Found internal URLs to endpoints.txt

        Response cookies to cookies.txt

        Response headers to headers.txt

 Modules Used
Module	Purpose
cloudscraper	Bypasses Cloudflare and other bot protections to get HTML.
urllib.parse	Resolves relative URLs and parses domains.
re	Regex to find href/src in HTML.
sys	Handles command-line input.
 Key Functions
extract_urls(html, base_url)

    Uses regex to find all href="..." or src="..." links.

    Converts them to absolute URLs using urljoin.

    Filters out external domains (keeps only same domain or subdomain).

    Returns a set of clean internal URLs.

🛠 Usage

python script.py https://example.com

Outputs:

    endpoints.txt – all internal links found

    cookies.txt – session cookies (useful for authenticated scraping)

    headers.txt – server response headers

 Use Cases

    Bug bounty recon

    Initial page crawling

    Fingerprinting headers + cookies

    Gathering JS/CSS/image endpoints

 Why Use cloudscraper?

Unlike requests, cloudscraper handles anti-bot JavaScript challenges automatically (like from Cloudflare). Useful for scraping modern, protected websites.

Let me know if you want to extend this (e.g. JavaScript URL extraction, recursive crawling, saving JS file content, etc).
