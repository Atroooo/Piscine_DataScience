def NULL_not_found(object: any) -> int:
    if type(object) is float and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif type(object) is int and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif type(object) is type(None) and object == object:
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif type(object) is str and object == "":
        print(f"Empty: {object} {type(object)}")
    elif type(object) is bool and object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    else:
        print("Type Not Found")
        return 1
