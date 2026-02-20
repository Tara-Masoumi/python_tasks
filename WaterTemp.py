while True:
    t = int(input("دمای آب را وارد کنید:"))
    if t > 100:
        print("Steam")
    elif t < 0:
        print("Ice")
    else:
        print("Water")

