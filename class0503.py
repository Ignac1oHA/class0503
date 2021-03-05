try:

    # First we read the age as characters

    age = input("How old are you?")

    # we try to convert the age to number
    age =int(age)



except ValueError:
    print("Sorry, but that is not a number")
except ZeroDivisionError:
    print("Can not divide by zero")
except:
    print("Something else happened")
else:
    print("you were bron around" , 2021 - age)
finally:
    print("Thanks for playing my game")