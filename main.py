from requests import get 

endpoint = "https://random-data-api.com/api/address/random_address"

data = {"size":10}

def main():
  
  r = get(endpoint,data).json()
  print(r)

if __name__ == "__main__":
   main()  

