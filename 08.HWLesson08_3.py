print("Enter the number of fishermen standing on the shore no more than 100 people")
num_of_fishermen = int(input())
if (num_of_fishermen > 100) or (num_of_fishermen < 0):
    print("The quantity entered does not meet the conditions.")
    quit()
print("Enter the maximum weight that one boat can support from 1 to 1 000 000")
weight_boat = float(input())
if (weight_boat > 1000000) or (weight_boat < 1):
    print("The quantity entered does not meet the conditions.")
    quit()
print("Enter the weight of each fisherman")
list_of_weight = []
for i in range(num_of_fishermen):
    weight_fisherman = int(input())
    list_of_weight.append(weight_fisherman)
count = 0
list_without_fatties = []
for i in range(len(list_of_weight)):
    if list_of_weight[i] > weight_boat:
        count += 1
        num_of_fishermen -= 1
    else:
        list_without_fatties.append(list_of_weight[i])
list_without_fatties.sort()
list_of_weight.clear()
if (num_of_fishermen == 0):
    print("No boat can carry a single fisherman. Try to make a raft out of boats or find a bigger boats.")
    quit()
elif (num_of_fishermen != 0) and (count != 0):
    print("The number of fishermen who cannot be transported by boat is", count)
    print("The number of fishermen who can be transported by boat is", num_of_fishermen)
else: 
    print("The number of fishermen who can be transported by boat is", num_of_fishermen)
count_of_board = 0
while num_of_fishermen > 0:
    if  num_of_fishermen == 1: # если рыбак всего один, либо остался один, то потребовалась бы всего одна лодка
        count_of_board += 1
        num_of_fishermen -= 1
    elif list_without_fatties[0] > weight_boat//2: # если даже самый худой весит больше половины лодки, то каждому потребуется отдельная лодка
        count_of_board = num_of_fishermen
        num_of_fishermen = 0
    elif list_without_fatties[0] + list_without_fatties[-1] > weight_boat: # в данном случае крепыша придется перевозить на отдельной лодке
        count_of_board += 1
        num_of_fishermen -= 1
        list_without_fatties.pop()
    elif list_without_fatties[0] + list_without_fatties[-1] <= weight_boat: # если двое могут переплыть, то весла им в руки 
        print(list_without_fatties)
        count_of_board += 1
        num_of_fishermen -=2
        list_without_fatties.pop()
        list_without_fatties.pop(0)
        print(list_without_fatties)
print("The minimum number of boats required for a one-time transportation of fishermen to the other side is:")
print(count_of_board, "boards")
print("The number of fishermen left on the shore is:", count+num_of_fishermen)
print("PS. According to the condition of the problem, only two can be in the boat, but it is not indicated whether one of the fishermen takes control of the boat. In this regard, the calculation is based on a one-time transportation of all fishermen.")
