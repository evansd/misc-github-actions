import sys

import bs4
import requests


def main():
    cookies = {}
    headers = {
        "authority": "www.freepeople.com",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cache-control": "max-age=0",
        "dnt": "1",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    }

    params = {
        "category": "fleece-jackets",
        "color": "040",
        "type": "REGULAR",
        "quantity": "1",
    }
    url = "https://www.freepeople.com/uk/shop/hit-the-slopes-colorblock-jacket/"
    response = requests.get(url, params=params, cookies=cookies, headers=headers)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    size_status = {
        size: soup.find(
            id=f"size-{size_id}-pdp-hit-the-slopes-colorblock-jacket"
        ).attrs.get("disabled")
        != "disabled"
        for size, size_id in [
            ("XS", 4000),
            ("S", 5000),
            ("M", 6000),
        ]
    }
    if any(available for available in size_status.values()):
        print(size_status)
        sys.exit(1)


if __name__ == "__main__":
    main()
