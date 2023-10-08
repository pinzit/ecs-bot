print("                               ___.              __   ")
print("   ____    ____    ______      \_ |__    ____  _/  |_ ")
print(" _/ __ \ _/ ___\  /  ___/       | __ \  /  _ \ \   __\ ")
print(" \  ___/ \  \___  \___ \        | \_\ \(  <_> ) |  |  ")
print("  \___  > \___  >/____  >       |___  / \____/  |__|  ")
print("      \/      \/      \/            \/                ")
print(" by theodore")
print("-------------------------------------------------------")

import time
import webbrowser
import requests
import re

def get_join_script_url(place_id, cookie):
  url = "https://ecsr.io/game/get-join-script?placeId=" + str(place_id)
  response = requests.get(url, cookies=cookie)

  if response.status_code != 200:
    print("failed to get join script URL: " + str(response.status_code))
    raise Exception("failed to get join script URL: " + str(response.status_code))

  json_data = response.json()
  join_script_url = json_data["joinScriptUrl"]

  return join_script_url

def get_join_script_ticket(join_script_url):
  match = re.search(r"https://ecsr.io/placelauncher.ashx\?ticket=(.*)", join_script_url)
  if match is None:
    print("failed to get join script ticket")
    raise Exception("failed to get join script ticket")

  return match.group(1)

def launch_app(url):
  webbrowser.open(url)

def main():
  place_id = YOUR_PLACE_ID
  cookie = {".ROBLOSECURITY": "YOUR_COOKIE"}

  join_script_url = get_join_script_url(place_id, cookie)
  join_script_ticket = get_join_script_ticket(join_script_url)

  print("join script URL:", join_script_url)
  print()
  print("join script ticket:", join_script_ticket)
  print()

  url = "ecsr-player://1+launchmode:play+gameinfo:{ticket}+placelauncherurl:{url}+k:l".format(url=join_script_url, ticket=join_script_ticket)

  launch_app(url)
  print("joined the game")
  print()

  while True:
    time.sleep(603)

    join_script_url = get_join_script_url(place_id, cookie)
    join_script_ticket = get_join_script_ticket(join_script_url)

    url = "ecsr-player://1+launchmode:play+gameinfo:{ticket}+placelauncherurl:{url}+k:l".format(url=join_script_url, ticket=join_script_ticket)

    launch_app(url)
    print("10 minutes are up, new game")

if __name__ == "__main__":
  main()
