def get_student_result(marks):
    if len(marks) != 5:
        raise ValueError("Exactly five marks are required")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Each mark must be between 0 and 100")

    total = sum(marks)
    percentage = total / 5

    return {
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "passed": all(mark >= 40 for mark in marks),
    }
