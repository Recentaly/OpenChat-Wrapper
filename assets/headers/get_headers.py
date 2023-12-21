from ..typing import Headers

def get_headers() -> Headers:

    """Get default headers for simple request headers."""
    return {
    'Host': 'openchat.team',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://openchat.team/',
    'Content-Type': 'application/json',
    'Content-Length': '183',
    'Origin': 'https://openchat.team',
    'Alt-Used': 'openchat.team',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'TE': 'trailers'
}


# Path: assets/headers/get_headers.py