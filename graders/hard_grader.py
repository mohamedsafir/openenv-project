def grade_hard(output, task):
    output = output.replace(" ", "")

    if "a/b" in output:
        return 1.0
    elif "/" in output:
        return 0.5
    else:
        return 0.0
