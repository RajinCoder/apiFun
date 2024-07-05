import requests
import pandas as pd
import sqlalchemy as db

url = 'https://api.sportmonks.com/v3/football/players'
header = {'Authorization': '8VXrDStCmKp2kNnZHwoaYv3mMYCA3oAwJcRqxzg5f5k4k8Ek3bNv7J5AhWqd'}

response = requests.get(url, headers=header)

if response.status_code != 200:
    raise Exception("API request failed with status code " + str(response.status_code))

engine = db.create_engine('sqlite:///soccer_players.db')

array_of_dict = response.json().get('data', [])
playerInfo = []

for row in array_of_dict:
    playerInfo.append({
        'name': row.get('name'),
        'id': row.get('id'),
        'position_id': row.get('position_id'),
        'nationality_id': row.get('nationality_id'),
        'height': row.get('height'),
        'weight': row.get('weight'),
        'date_of_birth': row.get('date_of_birth')
    })

pdFrame = pd.DataFrame(playerInfo)

pdFrame.to_sql('soccer_players', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
    query = db.text("SELECT * FROM soccer_players WHERE name='Daniel Munthe Agger';")
    query_result = connection.execute(query).fetchall()
    if query_result:
        print(pd.DataFrame(query_result, columns=pdFrame.columns))
    else:
        print("No results found.")
