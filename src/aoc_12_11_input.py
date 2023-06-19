import math


def check_intermed(val):
    if val > 11 * 2 * 5 * 7 * 17 * 19 * 3 * 13:
        return val % (11 * 2 * 5 * 7 * 17 * 19 * 3 * 13)
    return val


def get_input_dict_counts():
    monkey_dict = {
        "m0": [75, 63],
        "m1": [65, 79, 98, 77, 56, 54, 83, 94],
        "m2": [66],
        "m3": [51, 89, 90],
        "m4": [75, 94, 66, 90, 77, 82, 61],
        "m5": [53, 76, 59, 92, 95],
        "m6": [81, 61, 75, 89, 70, 92],
        "m7": [81, 86, 62, 87],
    }

    monkey_counts = {"m0": 0, "m1": 0, "m2": 0, "m3": 0, "m4": 0, "m5": 0, "m6": 0, "m7": 0}
    return monkey_dict, monkey_counts


def mky_opers(monkey, x, monkey_dict):
    if monkey == "m0":
        intermed = math.floor((x * 3) / 3)
        if intermed % 11 == 0:
            monkey_dict["m7"].append(intermed)
        else:
            monkey_dict["m2"].append(intermed)
    elif monkey == "m1":
        intermed = math.floor((x + 3) / 3)
        if intermed % 2 == 0:
            monkey_dict["m2"].append(intermed)
        else:
            monkey_dict["m0"].append(intermed)
    elif monkey == "m2":
        intermed = math.floor((x + 5) / 3)
        if intermed % 5 == 0:
            monkey_dict["m7"].append(intermed)
        else:
            monkey_dict["m5"].append(intermed)
    elif monkey == "m3":
        intermed = math.floor((x * 19) / 3)
        if intermed % 7 == 0:
            monkey_dict["m6"].append(intermed)
        else:
            monkey_dict["m4"].append(intermed)
    elif monkey == "m4":
        intermed = math.floor((x + 1) / 3)
        if intermed % 17 == 0:
            monkey_dict["m6"].append(intermed)
        else:
            monkey_dict["m1"].append(intermed)
    elif monkey == "m5":
        intermed = math.floor((x + 2) / 3)
        if intermed % 19 == 0:
            monkey_dict["m4"].append(intermed)
        else:
            monkey_dict["m3"].append(intermed)
    elif monkey == "m6":
        intermed = math.floor((x * x) / 3)
        if intermed % 3 == 0:
            monkey_dict["m0"].append(intermed)
        else:
            monkey_dict["m1"].append(intermed)
    elif monkey == "m7":
        intermed = math.floor((x + 8) / 3)
        if intermed % 13 == 0:
            monkey_dict["m3"].append(intermed)
        else:
            monkey_dict["m5"].append(intermed)

    return monkey_dict


def mky_opers_pt2(monkey, x, monkey_dict):
    if monkey == "m0":
        intermed = math.floor((x * 3))
        intermed = check_intermed(intermed)
        if intermed % 11 == 0:
            monkey_dict["m7"].append(intermed)
        else:
            monkey_dict["m2"].append(intermed)
    elif monkey == "m1":
        intermed = math.floor((x + 3))
        intermed = check_intermed(intermed)
        if intermed % 2 == 0:
            monkey_dict["m2"].append(intermed)
        else:
            monkey_dict["m0"].append(intermed)
    elif monkey == "m2":
        intermed = math.floor((x + 5))
        intermed = check_intermed(intermed)
        if intermed % 5 == 0:
            monkey_dict["m7"].append(intermed)
        else:
            monkey_dict["m5"].append(intermed)
    elif monkey == "m3":
        intermed = math.floor((x * 19))
        intermed = check_intermed(intermed)
        if intermed % 7 == 0:
            monkey_dict["m6"].append(intermed)
        else:
            monkey_dict["m4"].append(intermed)
    elif monkey == "m4":
        intermed = math.floor((x + 1))
        intermed = check_intermed(intermed)
        if intermed % 17 == 0:
            monkey_dict["m6"].append(intermed)
        else:
            monkey_dict["m1"].append(intermed)
    elif monkey == "m5":
        intermed = math.floor((x + 2))
        intermed = check_intermed(intermed)
        if intermed % 19 == 0:
            monkey_dict["m4"].append(intermed)
        else:
            monkey_dict["m3"].append(intermed)
    elif monkey == "m6":
        intermed = math.floor((x * x))
        intermed = check_intermed(intermed)
        if intermed % 3 == 0:
            monkey_dict["m0"].append(intermed)
        else:
            monkey_dict["m1"].append(intermed)
    elif monkey == "m7":
        intermed = math.floor((x + 8))
        intermed = check_intermed(intermed)
        if intermed % 13 == 0:
            monkey_dict["m3"].append(intermed)
        else:
            monkey_dict["m5"].append(intermed)

    return monkey_dict
