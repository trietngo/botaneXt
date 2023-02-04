import requests


def get_ip():
    response = requests.get("http://checkip.dyndns.org")
    ip_add = response.text.split(":")[-1].strip()
    return ip_add.split("<")[0]


def get_location(input_ip):
    response = requests.get(f"http://ipinfo.io/{input_ip}/json")
    data = response.json()
    return data["city"], data["region"], data["country"]


ip = get_ip() # get_ip() should be the function from the previous answer
print("Your ip is: ", ip)
location = get_location(ip)
print("Your location is:", location)