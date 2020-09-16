def input_number(text):
    number = 0
    try:
        number = int(input(text))
    except:
        pass
    if 0 < number < 21:
        if verify(number):
            print("Valid")
            return number
        else:
            return input_number(text)
    else:
        print("Please enter a valid number")
        return input_number(text)

def verify(n):
    text = "Do you mean " + str(n) + " ? Enter Y/N: "
    ans = input(text)
    if ans == "Y":
        return True
    elif ans == "N":
        return False
    else:
        print("Please enter Y or N")
        return verify(n)

num = input_number("Please enter a number between 1 to 20 to display its timestable: ")
times = input_number("Please enter a number between 1 to 20 for the number of rows you want to display: ")

for i in range(1,times+1):
    print(num,"x",i,"=",num*i)
