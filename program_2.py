# Nathan Parker
# 03/07/25
# Program #2: Larger than n

# define the main function
def main():

    # set n equal to any value
    n = 7

    # create an empty list
    list1 = []

    # fill the list
    for index in range(1,21):
        list1.append(index)

    # call the function
    function(list1,n)

# define a function that displays only the values greater than n
def function(l,n):
    l = [l for l in range(1,21) if l > n]
    print(l)

# call the main function
if __name__ == '__main__':
    main()

