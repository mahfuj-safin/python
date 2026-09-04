# sum of 5 numbers from a list

numbers = input("Enter the 5 numbers: ").split()
numbers = [int(i) for i in numbers]
def sum_list(numbers):

  total = 0
  for i in numbers:
    total += i

  return total

result = sum_list(numbers)
print(result)