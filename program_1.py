# Nathan Parker
# 03/07/25
# Program #1: Rainfall

# define the main function
def main():

    # create an empty list
    rainfall = []

    # get the rainfall for each month from the user and add the values to the rainfall list
    for loop in range(12):
        month = float(input('Enter the total rainfall for a month: '))
        rainfall.append(month)

    # calculate and display the results
    print(f'''Total rainfall: {sum(rainfall)}
Average rainfall: {sum(rainfall)/12}
Highest rainfall: {max(rainfall)}
Lowest rainfall: {min(rainfall)}''')

# call the main function
if __name__ == '__main__':
    main()
