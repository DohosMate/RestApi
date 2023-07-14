import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 1, "name": "Mate", "views": 2},
        {"likes": 10, "name": "Bea", "views": 4},
        {"likes": 100, "name": "Pulya", "views": 8}]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())
    
input()
response = requests.patch(BASE + 'video/1', {"likes": 1000, "name": "Bea", "views": 200})

input()
response = requests.get(BASE + 'video/1')
print(response.json())

input()
response = requests.delete(BASE + 'video/1')
print("DELETED")


