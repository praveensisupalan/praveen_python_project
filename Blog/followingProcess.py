import json
import random

with open("following.json") as file:
    profilData = json.load(file)

user1follower = [user["followers"] for user in profilData if user['id'] == 1]
# print(user1follower[0])

OtherUsers = []
for user in profilData:
    if user["id"] not in user1follower[0] and user["id"] != 1:
        OtherUsers.append(user["id"])

randomSele = random.sample(OtherUsers, 2)

for id in randomSele:
    for user in profilData:
        if id == user["id"]:
            print(f"userid=", user["id"], "username=", user["username"])
