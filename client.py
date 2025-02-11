import requests

response = requests.get("http://192.168.187.4:5000/message")
print("Response from VM2:", response.json())
