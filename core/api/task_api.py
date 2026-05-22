import json
from core.storage.file_handler import read_data, write_data


class TaskAPI:

    def create_task(self, request):
        try:
            data = json.loads(request)

            if not data.get("title"):
                raise Exception("Task title required")

            boards = read_data("boards.json")
            users = read_data("users.json")
            tasks = read_data("tasks.json")

            # validate board
            board = next((b for b in boards if b["id"] == data.get("board_id")), None)
            if not board:
                raise Exception("Board not found")

            # validate user
            user = next((u for u in users if u["id"] == data.get("assigned_to")), None)
            if not user:
                raise Exception("User not found")

            new_task = {
                "id": max([t["id"] for t in tasks], default=0) + 1,
                "title": data["title"],
                "board_id": data["board_id"],
                "assigned_to": data["assigned_to"],
                "status": "todo"
            }

            tasks.append(new_task)
            write_data("tasks.json", tasks)

            return json.dumps({
                "message": "Task created successfully",
                "task": new_task
            })

        except Exception as e:
            return json.dumps({"error": str(e)})


    def get_tasks(self):
        try:
            return json.dumps({"tasks": read_data("tasks.json")})
        except Exception as e:
            return json.dumps({"error": str(e)})


    # ⭐ IMPORTANT: STATUS UPDATE (REQUIRED IN REQUIREMENT)
    def update_task_status(self, request):
        try:
            data = json.loads(request)

            tasks = read_data("tasks.json")

            task = next((t for t in tasks if t["id"] == data.get("task_id")), None)
            if not task:
                raise Exception("Task not found")

            allowed = ["todo", "in_progress", "done"]

            if data.get("status") not in allowed:
                raise Exception("Invalid status")

            task["status"] = data["status"]

            write_data("tasks.json", tasks)

            return json.dumps({
                "message": "Task status updated",
                "task": task
            })

        except Exception as e:
            return json.dumps({"error": str(e)})