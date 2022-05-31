def Reverse_List(List):
    reversed_list = []
    for i in range(len(List)-1,-1,-1):
        reversed_list.append(List[i])
    return reversed_list

array = input('enter the array to be reversed')
print(Reverse_List(array))