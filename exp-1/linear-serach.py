# Linear Search Algorithm
# The code recieves a list of numbers
# it then splits the inputed numbers into seperete elements in a list
# we get the target number from the user to search for in the list
# we then find the number from the list
# if the number is not found we return numeber not found
# if yes, we print the position of the number in the list

# time complextion O(n)
# space complextion O(1)

data = input("Enter numbers separated by spaces: ").strip()
numbers = [ int(x) for x in data.split() ]

target = int(input("Enter the number to search for: "))

for i in range(len(numbers)):
    if (numbers[i] == target ):
        print("Number found at index:", i)
        break
else:
    print("Number not found")