# sum of 5 numbers from a list


def sum_list(numbers):

  total = 0
  for i in numbers:
    total += i

  return total

# input
numbers = input("Enter the numbers: ").replace("," , " ").split()  #Here, the replace function works. If someone gives the numbers with commas, it will remove the commas and make them into spaces, for example: 25,45,54 -> 25 45 54. The function of split is to separate each number from the space it finds and create a string.

numbers = [int(i) for i in numbers]  #Here the value of numbers is taken from i and the values ​​of i are made integers.

# function call
result = sum_list(numbers)
print(result)



# -------------------------------------------------------------------
# Since Python is case sensitive, I have written the above in uppercase only, since the problem is the same.

def SUM_LIST(NUMBERS):

  TOTAL = 0
  for i in NUMBERS:
    TOTAL += i

  return TOTAL


RESULT = SUM_LIST([25,45,74,85,95])
print(RESULT)