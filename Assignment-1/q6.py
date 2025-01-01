# Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
for j in list1:
    if j % 3 == 0:
        print(j, "is divisible by 3")
    else:
        print(j, "is not divisible by 3")
