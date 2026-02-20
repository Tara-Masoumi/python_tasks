def sum(number):
    sum_digits = 0
    for digit in number:
        sum_digits += int(digit)

    print (sum_digits)

while True:
    number = input("عدد را وارد کنید")
    sum(number)