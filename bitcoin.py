import sys

import requests

API_KEY = "YOUR_API_KEY_HERE"
URL = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"


def get_amount():
    """Read and validate the command-line argument."""
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_price():
    """Return the current price of 1 BTC in USD."""
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        return float(response.json()["data"]["priceUsd"])
    except (requests.RequestException, KeyError, ValueError):
        sys.exit("Could not retrieve Bitcoin price")


def main():
    amount = get_amount()
    cost = amount * get_price()
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()
