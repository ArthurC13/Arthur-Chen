def input_number(text):                                                                                     #function for validation + input
    number = 0                                                                                              #define number
    try:                                                                                                    #validate if the input is an integer or not
        number = int(input(text))
    except:
        pass
    if 0 < number < 21:                                                                                     #validate if the input is in range or not
        if verify(number):                                                                                  #call verify function if number is in range
            print("Valid")
            return number                                                                                   #recall input_number if verify return False - allow user to re-enter a number
        else:
            return input_number(text)
    else:                                                                                                   #output a message if the number is not valid
        print("Please enter a valid number")
<<<<<<< Updated upstream
        return input_number(text)
# end function
=======
        return input_number(text)                                                                           #recall input_number so the user can re-enter a number
>>>>>>> Stashed changes

def verify(n):                                                                                              #function for verification
    text = "Do you mean " + str(n) + " ? Enter Y/N: "
    ans = input(text)                                                                                       #ask the user if the number is what they want
    if ans == "Y":                                                                                          #return True if the user confirms the number is what they want
        return True
    elif ans == "N":                                                                                        #return False if the user confirms the number is no what they want
        return False
    else:                                                                                                   #recall verify if the input is neither Y or N - allow user to re-enter a choice
        print("Please enter Y or N")
        return verify(n)
# end function

num = input_number("Please enter a number between 1 to 20 to display its timestable: ")                     #ask for the number
times = input_number("Please enter a number between 1 to 20 for the number of rows you want to display: ")  #ask for the number of rows

for i in range(1,times+1):                                                                                  #print out the times table
    print(num,"x",i,"=",num*i)
## ACS - Good this works well. You need to put comments in the code.
## ACS - I have added a couple 
