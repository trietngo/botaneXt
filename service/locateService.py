import requests


def get_ip():
    response = requests.get("http://checkip.dyndns.org")
    ip_add = response.text.split(":")[-1].strip()
    return ip_add.split("<")[0]


def get_location(input_ip):
    response = requests.get(f"http://ipinfo.io/{input_ip}/json")
    data = response.json()

    # both South and North San Francisco are treated as 'San Francisco'
    # temporary solution, need to improve the database in the future
    if data["city"] == "South San Francisco":
        data["city"] = "San Francisco"

    return data["city"]


ip = get_ip() # get_ip() should be the function from the previous answer
print("Your ip is: ", ip)
location = get_location(ip)
print("Your location is:", location)