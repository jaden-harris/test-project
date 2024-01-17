import requests

api_key = '3ecb5343a573f1d543835c06876dfb95'
city = "London"

url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid="+api_key

request = requests.get(url)
json = request.json()

min_temp = json.get("main").get("temp_min")
max_temp = json.get("main")['temp_max']
print("The minimum temp is: " + str(min_temp))
print("The maximum temp is : " + str(max_temp))