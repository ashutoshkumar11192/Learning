print('Welcome to the tip calculator')
while True:
    try:
        total_bill  = int(input("PLease enter total value"))
    except Exception as e:
        print("Print a valid number")
    else:
        print('Your bill amount is '+ str(total_bill))
        break
no of people
percentage of tip

while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
    else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        break



        # HFEfkjadsjj
