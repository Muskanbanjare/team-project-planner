import json
from core.storage.file_handler import read_data, write_data


class BoardAPI:

    def create_board(self, request):
        try:
            data = json.loads(request)

            if not data.get("board_name"):
                raise Exception("Board name is required")

            if not data.get("team_id"):
                raise Exception("Team ID is required")

            teams = read_data("teams.json")

            team_exists = any(t["id"] == data["team_id"] for t in teams)
            if not team_exists:
                raise Exception("Team not found")

            boards = read_data("boards.json")

            new_board = {
                "id": max([b["id"] for b in boards], default=0) + 1,
                "board_name": data["board_name"],
                "team_id": data["team_id"]
            }

            boards.append(new_board)
            write_data("boards.json", boards)

            return json.dumps({
                "message": "Board created successfully",
                "board": new_board
            })

        except Exception as e:
            return json.dumps({"error": str(e)})


    def get_boards(self):
        try:
            return json.dumps({"boards": read_data("boards.json")})
        except Exception as e:
            return json.dumps({"error": str(e)})