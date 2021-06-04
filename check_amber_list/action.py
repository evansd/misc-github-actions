from bs4 import BeautifulSoup
import requests


def main():
    response = requests.get(
        "https://www.gov.uk/guidance/red-amber-and-green-list-rules-for-entering-england"
    )
    response.raise_for_status()
    page = BeautifulSoup(response.text, "lxml")
    th = page.find(lambda tag: tag.name == "th" and "United States" in tag.get_text())
    row_text = th.find_parent("tr").find("td").get_text().strip()
    if row_text:
        raise ValueError(f"\n\n{row_text}\n\n")


if __name__ == "__main__":
    main()
