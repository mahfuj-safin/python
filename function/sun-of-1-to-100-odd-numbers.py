# sum of odd number 1 to 100

def sumOddNumbers():

  total = 0
  for i in range(1, 101):
    if(i % 2 != 0):
      total += i 
  return total

result = sumOddNumbers()
print(result)
