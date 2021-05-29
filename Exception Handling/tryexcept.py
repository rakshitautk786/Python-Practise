while (True):
    print("Press q to exit")
    a=int(input())
    if a=="q":
        break
    try:
        if a>6:
            print("No is not greater than 6")
    except Exception as e :
        print(f"You got error:{e}")

