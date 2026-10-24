import requests
location = input("enter your city")
url = f"https://api.weatherapi.com/v1/current.json?key=0a398942cb8a4152ad295922262410&q=nairobi"
response = requests.get(url)

if response.status_code == 200:
   data = response.json()

print(f"in {location}, the temperature is {data["current"]["temp_c"]} degrees celcius,and the weather is {data["current"]["condition"]["text"]}"=-------------))))