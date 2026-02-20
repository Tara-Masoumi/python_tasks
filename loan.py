def vam(age, incom):
    if age >= 18 and incom >= 5000000:
        print("شما واجد شرایط وام هستید")
    elif age < 18 or incom < 5000000:
        print("سن یا درآمد مجاز نیست")

while True:
    age = int(input("enter your age: "))
    income = int(input("enter your income: "))
    vam(age, income)