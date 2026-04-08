def grade_easy(output, task):
    output = output.lower()

    if "spam" in output:
        return 1.0
    elif any(word in output for word in task["keywords"]):
        return 0.5  # partial understanding
    else:
        return 0.0
