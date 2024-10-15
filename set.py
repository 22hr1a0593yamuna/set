# set
1) Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 

def print_sorted_set():
    n = int(input())
    values_set = set()
    for _ in range(n):
        value = int(input())
        values_set.add(value)
    sorted_values = sorted(values_set)
    print(" ".join(map(str, sorted_values))
print_sorted_set()
2) Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
def print_sorted_set_from_input():
    values_set = set(map(int, input().split()))
    sorted_values = sorted(values_set)
    print(" ".join(map(str, sorted_values)))
print_sorted_set_from_input()

3) Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3

def print_different_values():
    set1 = set(map(int, input().split()))
    set2 = set(map(int, input().split()))
    difference = set1 - set2
    sorted_difference = sorted(difference)
    print(" ".join(map(str, sorted_difference)))
print_different_values()


4) Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
def delete_element_from_set():
    values_set = set(map(int, input().split()))
    element_to_delete = int(input())
    if element_to_delete in values_set:
        values_set.remove(element_to_delete)
        # Print the updated set
        print(" ".join(map(str, sorted(values_set))))
    else:
        print("Given value is not present in the set list.")
delete_element_from_set()

5) Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 

def print_common_values():
    set2 = set(map(int, input().split()))
    common_values = set1 & set
    sorted_common_values = sorted(common_values)
    print(" ".join(map(str, sorted_common_values)))
print_common_values()

6)
Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
Sample Input:
1 2 3 4 5 1 2 3
Sample Output:
5
def count_unique_elements():
    values = list(map(int, input().split()))
    unique_values = set(values)
    print(len(unique_values))
count_unique_elements()

7) Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
def find_max_min_in_set():
    values_set = set(map(int, input().split()))
    max_value = max(values_set)
    min_value = min(values_set)
    print(f"Maximum: {max_value}")
    print(f"Minimum: {min_value}")
find_max_min_in_set()

8) Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
def update_set_with_another():
    set1 = set(map(int, input().split()))
    set2 = set(map(int, input().split()))
    set1.update(set2)
    updated_values = sorted(set1)
    print(" ".join(map(str, updated_values)))
update_set_with_another()
9) Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
def count_duplicates_and_print_unique():
    n = int(input())
    values = []
    for _ in range(n):
        value = int(input())
        values.append(value)
    unique_values = set(values)
    duplicate_count = len(values) - len(unique_values)
    print(f"Duplicate Values: {duplicate_count}")
    print(" ".join(map(str, sorted(unique_values))))
count_duplicates_and_print_unique()




