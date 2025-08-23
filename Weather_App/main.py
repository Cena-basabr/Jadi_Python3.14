import requests

API_KEY = "YOUR_API_KEY"

city_name = input("نام شهر مورد نظر را وارد کنید: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data['cod'] == 200:
    city = data['name']
    temp = data['main']['temp']
    description = data['weather'][0]['description']

    print("\n--------------------")
    print(f"آب و هوا در {city}:")
    print(f"دما: {temp}°C")
    print(f"توضیحات: {description}")
    print("--------------------")
else:
    print("\nخطایی از سرور دریافت شد. پاسخ کامل سرور:")
    print(data)