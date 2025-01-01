# Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
count = 0
while a % b == 0:
    a = a / b
    count += 1
if count == 0:
    print("A is not divisible by B")
else:
    print(count)