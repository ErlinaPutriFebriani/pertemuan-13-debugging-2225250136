def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

test_cases = [59, 60, 61]
for test in test_cases:
    print(f"Nilai: {test} -> Status: {status_lulus(test)}")