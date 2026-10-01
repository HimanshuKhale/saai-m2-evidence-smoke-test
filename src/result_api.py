@"
def get_student_result(student_id):
    if not student_id:
        raise ValueError("student_id is required")

    return {
        "student_id": student_id,
        "status": "success",
        "result": {
            "score": 82,
            "grade": "A"
        }
    }
"@ | Set-Content src/result_api.py