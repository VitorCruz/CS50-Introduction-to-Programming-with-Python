
import requests
import sys
import json

## SEE IF NUMBER OF ARGUMENTS == 2
if len(sys.argv) != 2:
    sys.exit("Invalid number of arguments at command-line")

## TRY TO CONVERT SECOND ARGUMENT TO FLOAT
try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Number of bitcoins must be a number")

## REQUEST BITCOIN PRICE AT COINDESK API'S
try:
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url).json()
except requests.RequestException:
    sys.exit("Request Error")

bitcoin_cost = float(response["bpi"]["USD"]["rate_float"])
total_cost = n * bitcoin_cost

print(f'Bitcoin cost = {bitcoin_cost:,.4f}')
print(f'Final cost = {total_cost:,.4f}')
