print("Enter the number of list elements from 1 to 100 000:")
number = int(input())
if (number < 1) or (number > 100000):
    print("You entered a number of list elements less than 1 or greater than 100 000. Please try again.")
    quit()
else:
    print("Enter number elements to the list from 1 to 1 000 000 000 by space")
    list1 = list(map(int, input().split()))
    for i in list1:
        if i > 1000000000:
            print("One or more of the entered items is greater than 1 000 000 000")
            quit()
    result = []
    if len(list1) != number:
        print("You entered items that do not match the specified number")
    else:
        print("Elements entered in the list:")
        print(list1)
        result.append(list1[-1])
        for i in range(len(list1)-1):
            result.append(list1[i])
        print("Elements modify in the list:")
        print(result)
