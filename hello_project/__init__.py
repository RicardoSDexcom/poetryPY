import requests

def get_solana_price_in_mxn():
    # CoinGecko API endpoint for SOL price in MXN
    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=mxn"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            solana_data = response.json()
            solana_price_mxn = solana_data['solana']['mxn']
            return solana_price_mxn
        else:
            print("Failed to fetch data")
    except requests.RequestException as e:
        print("Error:", e)
        return None

# Get SOL price in MXN
solana_mxn_price = get_solana_price_in_mxn()
if solana_mxn_price is not None:
    print(f"The current price of Solana (SOL) in MXN is: {solana_mxn_price}")
