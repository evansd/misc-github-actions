import sys

import requests


SPEC = """
11016	24 East Avenue, Wellsboro, PA 16901
11036	1913 East 3rd Street, Williamsport, PA 17701
4415	14 Fifth Street, Williamsport, PA 17701
1830	77 Reuters Boulevard, Towanda, PA 18848
11084	148 Ennis Lane, Towanda, PA 18848
"""

STORES = [line.strip().split(maxsplit=1) for line in SPEC.strip().splitlines()]


def main():
    session = requests.session()
    available = []
    for store_id, address in STORES:
        response = session.get(
            f"https://www.riteaid.com/services/ext/v2/vaccine/checkSlots"
            f"?storeNumber={store_id}"
        )
        if response.json()["Data"]["slots"]["1"]:
            available.append(address)
    if available:
        print("Slots available at:")
        print("\n".join(available))
        return True


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
