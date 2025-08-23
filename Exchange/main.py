import requests

API_KEY = "API_KEY"

base_currency = input("ارز مبدأ را وارد کنید (مثلاً USD): ").upper()
target_currency = input("ارز مقصد را وارد کنید (مثلاً EUR): ").upper()
amount = float(input(f"مبلغ را به {base_currency} وارد کنید: "))

url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
response = requests.get(url)
data = response.json()

if data['result'] == 'success':
    conversion_rates = data['conversion_rates']

    target_rate = conversion_rates[target_currency]

    converted_amount = amount * target_rate

    print("\n--------------------")
    print(f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
    print("--------------------")
else:
    print("خطا: دریافت نرخ تبدیل ناموفق بود.")