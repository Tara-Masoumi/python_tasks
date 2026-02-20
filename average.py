def get_average():

    marks = []
    n = int(input("چند نمره میخوای وارد کنی:"))
    for i in range(n):
        score = int(input(f"نمره {i + 1} را وارد کن: "))
        marks.append(score)

    total = sum(marks)
    count = len(marks)
    return total // count

while True:
    result = get_average()
    print(f"میانگین گردشده: {result}")

