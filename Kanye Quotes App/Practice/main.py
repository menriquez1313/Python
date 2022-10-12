import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")


#print(response.status_code)

# if response.status_code != 200:
#     raise Exception("Bad response from ISS API") #General Type of Exception

# if response.status_code == 404:
#     raise Exception ("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.")

response.raise_for_status()

data = response.json()
#data = response.json()["iss_position"]["longitude"] #example for the use to get get specified info from the URL
#print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)

