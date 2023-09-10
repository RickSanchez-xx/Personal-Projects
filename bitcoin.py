import sys
import requests

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit(1)

else:
    bitcoin_dict = response.json()
    bitcoin_price = bitcoin_dict["bpi"]["USD"]["rate_float"]


if len(sys.argv) != 2:
    sys.exit("Missing-command line arg! ")
else:
    try:
        entry = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line is not a number! :(")
    else:
        print(f"${entry * bitcoin_price:,.4f}")
