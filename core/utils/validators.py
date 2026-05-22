def validate_user_data(data):

    # name validation
    if "name" not in data or not data["name"]:
        raise Exception("Name is required")

    # email validation
    if "email" not in data or not data["email"]:
        raise Exception("Email is required")