def grade_medium(output, task):
    output = str(output).replace(" ", "")

    if output == task.get("answer", ""):
        return 0.9
    elif all(x in output for x in ["1", "2", "3", "4", "5"]):
        return 0.5
    else:
        return 0.1
