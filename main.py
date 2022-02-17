import json

website = {
    "details": {
        "email": "joshuabayo88@yahoo.com",
        "password": "adejumoke"
    }
}

print(website.get("details").get("password"))

# with open ("website_data.json", "w") as data_file:
#     website_json = json.dump(website, data_file, indent=4)

with open ("website_data.json", "r") as read_data:
    load_data = json.load(read_data)
    print(load_data)
    load_data.update(website)

with open ("website_data.json", "w") as read_data:
    new_data = json.dump(website, read_data, indent=4)
# print(load_data)