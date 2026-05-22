import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planner.settings")
django.setup()

from core.api.user_api import UserAPI
from core.api.team_api import TeamAPI


user_api = UserAPI()
team_api = TeamAPI()


# CREATE USER
user_request = json.dumps({
    "name": "Muskan",
    "email": "muskan@gmail.com"
})

print("CREATE USER:")
print(user_api.create_user(user_request))

print("\n")


# CREATE TEAM
team_request = json.dumps({
    "team_name": "Backend Team"
})

print("CREATE TEAM:")
print(team_api.create_team(team_request))

print("\n")


# ADD USER TO TEAM
add_request = json.dumps({
    "team_id": 1,
    "user_id": 1
})

print("ADD USER TO TEAM:")
print(team_api.add_user_to_team(add_request))

print("\n")


# GET TEAMS
print("GET TEAMS:")
print(team_api.get_teams())