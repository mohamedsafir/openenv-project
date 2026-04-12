def grade_hard(output, task):
    output = str(output).replace(" ", "")

    if "a/b" in output:
        return 0.9
    elif "/" in output:
        return 0.5
    else:
        return 0.1  # NOT 0.0
