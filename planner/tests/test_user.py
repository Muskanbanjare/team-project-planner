import json
import os
import django

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planner.settings")
django.setup()

from core.api.user_api import UserAPI

# object create
user_api = UserAPI()


# CREATE USER
request_data = json.dumps({
    "name": "Muskan",
    "email": "muskan@gmail.com"
})

create_response = user_api.create_user(request_data)

print("CREATE USER:")
print(create_response)

print("\n")


# GET USERS
get_response = user_api.get_users()

print("GET USERS:")
print(get_response)

print("\n")


# DELETE USER
delete_response = user_api.delete_user(1)

print("DELETE USER:")
print(delete_response)

print("\n")


# FINAL USERS
final_response = user_api.get_users()

print("FINAL USERS:")
print(final_response)