from requests import get 

url = "https://random-data-api.com/api/restaurant/random_restaurant"
data = {"size":2}

r = get(url,data).json()

for i in r:
  print(i["id"])
  for dia in i["hours"]:
     if i["hours"][dia]["is_closed"] == True:
         print(dia,"Aberto")
     else:
         print(dia, "fechado")