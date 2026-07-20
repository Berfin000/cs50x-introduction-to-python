import sys
import requests
API_KEY= "4ddf731d450d6a1b6c5b4dc518463e91e8d0c45ba1623d7c5571ff8c456caac4"

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        bitcoin_amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
        response = requests.get(url)
        data_packet = response.json()
    except requests.RequestException:
        sys.exit("API request failed")

    bitcoin_price = float(data_packet["data"]["priceUsd"])
    total_cost = bitcoin_amount * bitcoin_price
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
