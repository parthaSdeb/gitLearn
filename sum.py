

list =[1,2,3,4,5,6,7,8,9]

## routine sum calculation
def sum(test_list):
    summation = 0
    #do actual summ
    for i in range (len(test_list)): summation += test_list[i]
    return summation


print(sum(list))
