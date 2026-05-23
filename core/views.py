import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.api.user_api import UserAPI
from core.api.team_api import TeamAPI
from core.api.board_api import BoardAPI

from core.api.task_api import TaskAPI
task_api = TaskAPI()

# API objects
user_api = UserAPI()
team_api = TeamAPI()
board_api = BoardAPI()


# -------------------------
# USERS API
# -------------------------

@csrf_exempt
def user_api_view(request, user_id=None):

    # CREATE USER
    if request.method == "POST":

        response = user_api.create_user(
            request.body.decode()
        )

        return JsonResponse(json.loads(response))

    # GET USERS
    if request.method == "GET":

        response = user_api.get_users()

        return JsonResponse(json.loads(response), safe=False)

    # UPDATE USER
    if request.method == "PUT":

        response = user_api.update_user(
            user_id,
            request.body.decode()
        )

        return JsonResponse(json.loads(response))

    # DELETE USER
    if request.method == "DELETE":

        response = user_api.delete_user(user_id)

        return JsonResponse(json.loads(response))

# -------------------------
# TEAMS API
# -------------------------

@csrf_exempt
def team_api_view(request, team_id=None):

    # CREATE TEAM
    if request.method == "POST":

        response = team_api.create_team(
            request.body.decode()
        )

        return JsonResponse(json.loads(response))

    # GET TEAMS
    if request.method == "GET":

        response = team_api.get_teams()

        return JsonResponse(json.loads(response), safe=False)

    # UPDATE TEAM
    if request.method == "PUT":

        response = team_api.update_team(
            team_id,
            request.body.decode()
        )

        return JsonResponse(json.loads(response))

    # DELETE TEAM
    if request.method == "DELETE":

        response = team_api.delete_team(team_id)

        return JsonResponse(json.loads(response))


@csrf_exempt
def add_user_to_team_view(request):

    try:
        if request.method == "POST":

            body = request.body.decode()

            response = team_api.add_user_to_team(body)

            return JsonResponse(json.loads(response))

        return JsonResponse({
            "error": "Only POST method allowed"
        }, status=405)

    except Exception as e:
        return JsonResponse({
            "error": str(e)
        }, status=500)


# -------------------------
# BOARDS API
# -------------------------


@csrf_exempt
def board_api_view(request, board_id=None):

    # CREATE BOARD
    if request.method == "POST":
        response = board_api.create_board(request.body.decode())
        return JsonResponse(json.loads(response))

    # GET ALL BOARDS
    if request.method == "GET":
        response = board_api.get_boards()
        return JsonResponse(json.loads(response), safe=False)

    # UPDATE BOARD
    if request.method == "PUT":
        response = board_api.update_board(
            board_id,
            request.body.decode()
        )
        return JsonResponse(json.loads(response))

    # DELETE BOARD
    if request.method == "DELETE":
        response = board_api.delete_board(board_id)
        return JsonResponse(json.loads(response))



# -------------------------
# TASK API
# -------------------------

@csrf_exempt
def task_api_view(request, task_id=None):

    # CREATE TASK
    if request.method == "POST":
        response = task_api.create_task(
            request.body.decode()
        )

        return JsonResponse(json.loads(response))

    # GET TASKS
    if request.method == "GET":
        response = task_api.get_tasks()

        return JsonResponse(json.loads(response), safe=False)

    # UPDATE TASK
    if request.method == "PUT":
        response = task_api.update_task(
            task_id,
            request.body.decode()
        )

        return JsonResponse(json.loads(response))

    # DELETE TASK
    if request.method == "DELETE":
        response = task_api.delete_task(task_id)

        return JsonResponse(json.loads(response))


@csrf_exempt
def task_status_view(request):

    if request.method == "PUT":

        response = task_api.update_task_status(
            request.body.decode()
        )

        return JsonResponse(json.loads(response))