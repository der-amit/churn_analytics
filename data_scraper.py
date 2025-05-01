import requests

url = 'https://assets.datacamp.com/production/repositories/1764/datasets/79c5446a4a753e728e32b4a67138344847b8f131/Churn.csv'

response = requests.get(url)

if response.status_code == 200:
    with open('churn.csv', 'w') as f:
        f.write(response.text)
    print("csv file saved as churn.csv")
    
else:
    print("Failed to retrieve data. Status code: {response.status_code}")
    

