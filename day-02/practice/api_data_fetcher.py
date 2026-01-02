import requests # type: ignore
API_KEY = "DA59SNR725WCOO4A"

url = "https://www.alphavantage.co/query"



def monthly_stock_market_data():
    query = f"query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey={API_KEY}"
    response = requests.get(url+query).json()

    for key, value in response.items():

        print(key)
monthly_stock_market_data()