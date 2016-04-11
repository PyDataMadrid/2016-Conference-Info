def decision_tree_model(age, distance):
    if distance >= 2283.11:
        if age >= 40.00:
            if distance >= 6868.86:
                if distance >= 8278.82:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        if age >= 54.50:
            if age >= 57.00:
                return True
            else:
                return False
        else:
            return True