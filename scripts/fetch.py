import random, time, requests

HEADER_BUNDLES = [
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    },
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 "
                      "(KHTML, like Gecko) Version/16.6 Safari/605.1.15",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.8",
    }
]

def get(url, timeout=20):
    headers = random.choice(HEADER_BUNDLES).copy()
    time.sleep(random.uniform(0.3, 1.1))  # jitter
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()
    return r.text
