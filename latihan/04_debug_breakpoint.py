def rata_rata(data):
    if len(data) == 0:
        return 0
    total = sum(data)
    return total / len(data)

data_test = [80, 90, 70]
print(f"Rata-rata: {rata_rata(data_test)}")