# function to convert KM to Miles
def converter():
    # while loop with formula
    while True:
        # request user input
        km_convert = float(input("Enter number of Kilometres:"))

        # formula to convert KM_to_Miles
        answer = str(km_convert * 0.621) + ' Miles'
        print(answer)

        
# call the function
converter()
