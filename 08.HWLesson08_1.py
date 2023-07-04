print("Enter the number of list elements:")
number = int(input())
list1 = []
print("Enter elements of the list from 1 to 10000:")
for i in range(number):
    element = int(input())
    if element < 1:
        print("You entered a number less than 1, which does not match the condition. Please try again.")
        quit()
    elif element > 10000:
        print("You entered a number greater than 10000. Please try again.")
        quit()
    else:
        list1.append(element)
print("Elements entered in the list:")
print(list1)
list1.reverse()
print("Reversed List Elements:")
print(list1)
