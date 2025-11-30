import requests

url = "https://call3.tgju.org/ajax.json?rev=sS6c6AGKSb5ba24j7ZZmhqj6ohg1z5qoIzCKE9nfC6jLfPOLLHFN7n27Po5J"
response = requests.get(url)
data = response.json()

# Access under 'current'
usd_price = data["current"]["price_dollar_rl"]["p"]
print(usd_price)
