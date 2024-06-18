import requests

url = 'https://api.sportmonks.com/v3/football/fixtures'
header = {'Authorization': '8VXrDStCmKp2kNnZHwoaYv3mMYCA3oAwJcRqxzg5f5k4k8Ek3bNv7J5AhWqd'}

response = requests.get(url, headers=header)

print(response.status_code)
#print(response.json())