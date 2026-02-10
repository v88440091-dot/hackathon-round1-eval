import subprocess

# Test cases: (input, expected_output)
test_cases = [
    ("2 3", "5"),
    ("10 20", "30"),
    ("-5 5", "0")
]

score = 0
marks_per_case = 10

for inp, expected in test_cases:
    try:
        output = subprocess.check_output(
            ["python", "solution.py"],
            input=inp,
            text=True,
            timeout=2
        ).strip()

        if output == expected:
            score += marks_per_case
    except Exception:
        pass

print(f"FINAL SCORE: {score}/{len(test_cases) * marks_per_case}")
