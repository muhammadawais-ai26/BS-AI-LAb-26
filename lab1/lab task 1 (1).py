
def check_scholarship(score, documents_complete,
                      attendance, disciplinary_hold):

    if score < 70:
        return "Not Eligible"

    if not documents_complete:
        return "Not Eligible"

    if attendance < 75:
        return "Not Eligible"

    if disciplinary_hold:
        return "Not Eligible"

    return "Eligible"



test_cases = [
    {
        "name": "Case 1: Normal Pass",
        "input": (85, True, 90, False),
        "expected": "Eligible"
    },
    {
        "name": "Case 2: Attendance Failure",
        "input": (80, True, 65, False),
        "expected": "Not Eligible"
    },
    {
        "name": "Case 3: Disciplinary Failure",
        "input": (90, True, 85, True),
        "expected": "Not Eligible"
    },
    {
        "name": "Case 4: Threshold Boundary",
        "input": (70, True, 75, False),
        "expected": "Eligible"
    }
]


for case in test_cases:
    score, documents, attendance, hold = case["input"]

    actual = check_scholarship(
        score, documents, attendance, hold
    )

    print("\n", case["name"])
    print("Input:", case["input"])
    print("Expected Result:", case["expected"])
    print("Actual Result:", actual)

    if actual == case["expected"]:
        print("Reason: Test passed.")
    else:
        print("Reason: Test failed.")
        