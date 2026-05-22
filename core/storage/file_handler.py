import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DB_FOLDER = os.path.join(BASE_DIR, "db")


def read_data(filename):

    file_path = os.path.join(DB_FOLDER, filename)

    with open(file_path, "r") as file:
        return json.load(file)


def write_data(filename, data):

    file_path = os.path.join(DB_FOLDER, filename)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)