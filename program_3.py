# Nathan Parker
# 03/07/25
# Program #3: US_Population


# define the main function
def main():

    # set answer to yes
    answer = 'yes'

    # create and empty list
    data = []

    # set row to 0
    row = 0

    # get data from the user and add it to the list
    while answer == 'yes' or answer == 'Yes':

        # add a row to the list
        data.append([0,0,0])

        # fill the row with data from the user
        data[row][0] = int(input('Enter the year: '))
        data[row][1] = str(input('Enter the state: '))
        data[row][2] = int(input('Enter the population: '))

        # increase row by one so that the program can fill more rows in the list
        row += 1

        # ask the user if they want to continue entering data
        answer = input('Would you like to enter more information? ("yes" or "no"): ')

    # get the year that needs to be summed from the user
    year = int(input('Enter a year: '))

    # define variables row_test and total
    row_test = 0
    total = 0

    # loop over the number of rows in the list
    for loop in range(row):

        # add the population for the correct year to the total
        if data[row_test][0] == year:
            total += data[row_test][2]

        # increase row_test by 1 so that the program can look at the next row
        row_test += 1

    # display the total
    print(f'The total population for all states in {year} is {total:,}.')

# call the main function
if __name__ == '__main__':
    main()

