def grade_medium(output, task):
    output = output.replace(" ", "")

    if output == task["answer"]:
        return 1.0
    elif all(x in output for x in ["1", "2", "3", "4", "5"]):
        return 0.5
    else:
        return 0.0
