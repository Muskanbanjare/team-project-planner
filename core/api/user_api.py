import json
from core.storage.file_handler import read_data, write_data
from core.utils.validators import validate_user_data


class UserAPI:

    def create_user(self, request):
        try:
            data = json.loads(request)

            validate_user_data(data)

            users = read_data("users.json")

            # duplicate email check
            for user in users:
                if user["email"] == data["email"]:
                    raise Exception("Email already exists")

            new_user = {
                "id": max([u["id"] for u in users], default=0) + 1,
                "name": data["name"],
                "email": data["email"]
            }

            users.append(new_user)
            write_data("users.json", users)

            return json.dumps({
                "message": "User created successfully",
                "user": new_user
            })

        except Exception as e:
            return json.dumps({"error": str(e)})


    def get_users(self):
        try:
            users = read_data("users.json")
            return json.dumps({"users": users})
        except Exception as e:
            return json.dumps({"error": str(e)})


    def delete_user(self, user_id):
        try:
            users = read_data("users.json")

            updated = []
            found = False

            for u in users:
                if u["id"] == user_id:
                    found = True
                    continue
                updated.append(u)

            if not found:
                raise Exception("User not found")

            write_data("users.json", updated)

            return json.dumps({"message": "User deleted successfully"})

        except Exception as e:
            return json.dumps({"error": str(e)})