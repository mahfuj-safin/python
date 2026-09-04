# sum of 5 numbers from a list

numbers = input("Enter the numbers: ").replace("," , " ").split()
numbers = [int(i) for i in numbers]
def sum_list(numbers):

  total = 0
  for i in numbers:
    total += i

  return total

result = sum_list(numbers)
print(result)



# -------------------------------------------------------------------
# 

def SUM_LIST(NUMBERS):

  TOTAL = 0
  for i in NUMBERS:
    TOTAL += i

  return TOTAL


RESULT = SUM_LIST([25,45,74,85,95])
print(RESULT)