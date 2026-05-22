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
def user_api_view(request):
    if request.method == "POST":
        response = user_api.create_user(request.body.decode())
        return JsonResponse(json.loads(response))

    if request.method == "GET":
        response = user_api.get_users()
        return JsonResponse(json.loads(response), safe=False)


# -------------------------
# TEAMS API
# -------------------------

@csrf_exempt
def team_api_view(request):
    if request.method == "POST":
        response = team_api.create_team(request.body.decode())
        return JsonResponse(json.loads(response))

    if request.method == "GET":
        response = team_api.get_teams()
        return JsonResponse(json.loads(response), safe=False)


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
def board_api_view(request):

    if request.method == "POST":
        response = board_api.create_board(request.body.decode())
        return JsonResponse(json.loads(response))

    if request.method == "GET":
        response = board_api.get_boards()
        return JsonResponse(json.loads(response), asafe=False)
    





@csrf_exempt
def task_api_view(request):

    try:
        if request.method == "POST":
            body = request.body.decode()

            if not body:
                return JsonResponse({"error": "Empty body"}, status=400)

            response = task_api.create_task(body)
            return JsonResponse(json.loads(response))

        if request.method == "GET":
            response = task_api.get_tasks()
            return JsonResponse(json.loads(response), safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    


@csrf_exempt
def task_update_view(request):
    if request.method == "POST":
        response = task_api.update_task_status(request.body.decode())
        return JsonResponse(json.loads(response))

    return JsonResponse({"error": "Only POST allowed"}, status=405)