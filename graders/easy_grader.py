def grade_easy(output, task):
    output = str(output).lower()

    if "spam" in output:
        return 0.9
    elif any(word in output for word in task.get("keywords", [])):
        return 0.5
    else:
        return 0.1  # NOT 0.0
