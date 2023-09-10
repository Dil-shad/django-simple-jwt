import requests

# Replace these with actual values
base_url = "http://127.0.0.1:8000/"
login_endpoint = "/auth/login/"

# User login credentials
email = "dlz611606@gmail.com"
password = "123456789"

# Create a dictionary with the login data
login_data = {
    "email": email,
    "password": password
}

# Send a POST request to the login endpoint
response = requests.post(base_url + login_endpoint, data=login_data)

# Parse the response JSON
response_data = response.json()

# Print the response status code and content
# print("Response Status Code:", response.status_code)
# print("Response Content:", response.text)

# Access the JWT tokens from the response data
# tokens = response_data.get("tokens", {})
# access_token = tokens.get("access")
# refresh_token = tokens.get("refresh")

# if access_token and refresh_token:
#     print("Access Token:", access_token)
#     print("Refresh Token:", refresh_token)
# else:
#     print("Tokens not found in response data.")

print(response_data["tokens"]["access"])
print(' REFRESH ' + response_data["tokens"]["refresh"])
