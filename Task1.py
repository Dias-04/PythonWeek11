def find_ue(list1, list2):
    return [element for element in list1 if element not in list2]

list1 = input("1: ").split()
list2 = input("2: ").split()

result = find_ue(list1, list2)

print(result)