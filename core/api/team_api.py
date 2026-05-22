import json
from core.storage.file_handler import read_data, write_data


class TeamAPI:

    def create_team(self, request):
        try:
            data = json.loads(request)

            if not data.get("team_name"):
                raise Exception("Team name is required")

            teams = read_data("teams.json")

            for t in teams:
                if t["team_name"] == data["team_name"]:
                    raise Exception("Team already exists")

            new_team = {
                "id": max([t["id"] for t in teams], default=0) + 1,
                "team_name": data["team_name"],
                "members": []
            }

            teams.append(new_team)
            write_data("teams.json", teams)

            return json.dumps({
                "message": "Team created successfully",
                "team": new_team
            })

        except Exception as e:
            return json.dumps({"error": str(e)})


    def get_teams(self):
        try:
            return json.dumps({"teams": read_data("teams.json")})
        except Exception as e:
            return json.dumps({"error": str(e)})


    def add_user_to_team(self, request):
        try:
            data = json.loads(request)

            teams = read_data("teams.json")
            users = read_data("users.json")

            team = next((t for t in teams if t["id"] == data["team_id"]), None)
            if not team:
                raise Exception("Team not found")

            user = next((u for u in users if u["id"] == data["user_id"]), None)
            if not user:
                raise Exception("User not found")

            if data["user_id"] in team["members"]:
                raise Exception("User already in team")

            team["members"].append(data["user_id"])

            write_data("teams.json", teams)

            return json.dumps({"message": "User added to team successfully"})

        except Exception as e:
            return json.dumps({"error": str(e)})