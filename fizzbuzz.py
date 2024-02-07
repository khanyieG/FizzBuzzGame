user= int(input("enter a number between 1-100: "))

def divisible_of_3(user):
    if user%3 ==0:
        print("FIZZ")

def divisible_of_5(user):
    if user%5 == 0:
        print("BUZZ")


if __name__ == "__main__":
    divisible_of_3(user)
    divisible_of_5(user)        