import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planner.settings")
django.setup()

from core.api.board_api import BoardAPI

board_api = BoardAPI()


# UPDATE TASK STATUS
update_request = json.dumps({
    "board_id": 1,
    "task_id": 1,
    "status": "completed"
})

update_response = board_api.update_task_status(update_request)

print("UPDATE TASK STATUS:")
print(update_response)

print("\n")


# GET BOARDS
boards_response = board_api.get_boards()

print("GET BOARDS:")
print(boards_response)