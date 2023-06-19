import math


def check_intermed(val):
    if val > 13 * 17 * 19 * 23:
        return val % (13 * 17 * 19 * 23)
    return val


def get_example_dict_counts():
    monkey_dict_example = {"m0": [79, 98], "m1": [54, 65, 75, 74], "m2": [79, 60, 97], "m3": [74]}
    monkey_counts_example = {"m0": 0, "m1": 0, "m2": 0, "m3": 0}
    return monkey_dict_example, monkey_counts_example


def mky_opers_example(monkey, x, monkey_dict):
    if monkey == "m0":
        intermed = math.floor((x * 19) / 3)
        if intermed % 23 == 0:
            monkey_dict["m2"].append(intermed)
        else:
            monkey_dict["m3"].append(intermed)
    elif monkey == "m1":
        intermed = math.floor((x + 6) / 3)
        if intermed % 19 == 0:
            monkey_dict["m2"].append(intermed)
        else:
            monkey_dict["m0"].append(intermed)
    elif monkey == "m2":
        intermed = math.floor((x * x) / 3)
        if intermed % 13 == 0:
            monkey_dict["m1"].append(intermed)
        else:
            monkey_dict["m3"].append(intermed)
    elif monkey == "m3":
        intermed = math.floor((x + 3) / 3)
        if intermed % 17 == 0:
            monkey_dict["m0"].append(intermed)
        else:
            monkey_dict["m1"].append(intermed)
    return monkey_dict


def mky_opers_example_pt2(monkey, x, monkey_dict):
    if monkey == "m0":
        intermed = math.floor((x * 19))
        intermed = check_intermed(intermed)
        if intermed % 23 == 0:
            monkey_dict["m2"].append(intermed)
        else:
            monkey_dict["m3"].append(intermed)
    elif monkey == "m1":
        intermed = math.floor((x + 6))
        intermed = check_intermed(intermed)
        if intermed % 19 == 0:
            monkey_dict["m2"].append(intermed)
        else:
            monkey_dict["m0"].append(intermed)
    elif monkey == "m2":
        intermed = math.floor((x * x))
        intermed = check_intermed(intermed)
        if intermed % 13 == 0:
            monkey_dict["m1"].append(intermed)
        else:
            monkey_dict["m3"].append(intermed)
    elif monkey == "m3":
        intermed = math.floor((x + 3))
        intermed = check_intermed(intermed)
        if intermed % 17 == 0:
            monkey_dict["m0"].append(intermed)
        else:
            monkey_dict["m1"].append(intermed)
    return monkey_dict
