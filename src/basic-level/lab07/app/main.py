import httpx
from client import ApiClient
from downloader import download_file

client = ApiClient()

print("===== USERS =====")

users = client.get_users()

print(users)


print("\n===== ERROR =====")

try:
    client.get_error()

except httpx.HTTPStatusError as e:
    print("Error HTTP:", e)


print("\n===== TIMEOUT =====")

try:
    client.get_slow()

except httpx.ReadTimeout:
    print("Timeout detectado")


print("\n===== STREAMING =====")

download_file()
