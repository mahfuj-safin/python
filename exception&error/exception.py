try:
  number = int(input("Enter Number: "))
  result = 10 / number
  print(result)
except ZeroDivisionError:
  print("wrong! you do not dived a number by 0.")
except ValueError:
  print("please provided a int number.")