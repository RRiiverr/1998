# Basic Tutorial
# Create two files in the same folder and name them "ids" and "working ids" (You can change their names by editing line 7 and 8)
# Deprecated until further notice
# Have fun finding your most requested ids
# Outdated

import requests

w = open("working ids.txt", "a")
f = open("ids.txt", "r")

def is_steam_customurl_taken(id):
    s = requests.Session()
    r = s.get("https://steamcommunity.com/id/%s" % id)
    if ("The specified profile could not be found.".lower() in r.text.lower()):
        return False
    return True

print("Checking ids." + "\n")

lines = f.readlines()
for line in lines:
    username = line.strip()
    is_taken = is_steam_customurl_taken(username)
    if is_taken:
        print("%s is under usage" % username)
    else:
        print("%s it's possibly not under use" % username)
        w.write(username + "\n")

w.close()
f.close()

print("Finalized search")
print("Open your working ids(or whatever you named it to) folder to check them out")
input("Close me")
