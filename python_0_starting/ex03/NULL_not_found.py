def NULL_not_found(object: any) -> int:

    object_list = {
        None: "Nothing",
        '0': "Zero",
        '': "Empty",
        False: "Fake",
    }
    
    type_name = object_list.get(object, "Type not Found")

    if type(object) is float and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif object == 0 and type(object) is int:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif type_name == "Type not Found":
        print(type_name)
        return 1
    else:
        print(f"{type_name}: {object} {type(object)}")
    return 0
