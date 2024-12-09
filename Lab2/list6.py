list1 = [int(x) for x in input("Enter the first list of integers: ").split()]
list2 = [int(x) for x in input("Enter the second list of integers: ").split()]


if len(list1) == len(list2):
    print("Both lists have the same length:", len(list1))
else:
    print("Both lists do not have the same length.")


if sum(list1) == sum(list2):
    print("Both lists sum to the same value:", sum(list1))
else:
    print("Both lists do not sum to the same value.")


common_elements = set(list1) & set(list2)
if common_elements:
    print("Common Elements from both lists are:", common_elements)
else:
    print("There are no Common Elements in both lists.")

