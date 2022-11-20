import requests

# hostname: https://jsonplaceholder.typicode.com
# hostname: 172.67.155.7, 104.21.58.30
response = requests.get('http://127.0.0.1:8000/todos/1')

print(response.json())
print(response.status_code)
# print(response.headers)