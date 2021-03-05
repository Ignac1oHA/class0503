while True:


    try:
        gross = int(input("What is the gross?" ))

        kids = int(input("How many kids do you have"))

    except ValueError:

        print("Please use correct numbers")

# avoid cheaters
if kids > 10:
        kids = 10

# oNCE WE ARE HERE, WE HAVE PROPER NUMBERS
        tax = 0

if gross < 1000:
        tax = 10

elif gross < 2000:
        tax = 12

elif gross < 4000:
        tax = 14
else:
    # it means more or equal to 4000
        tax = 18
if goss < 2000:
        tax = tax - (kids*1)
else:
        tax = tax - (kids*0.5)

print("with a gross of", gross, "and", kids, "kids you take home" gross * (100-tax)/100)
