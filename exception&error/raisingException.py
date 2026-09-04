def check_age(age):
  assert age != 0, "Age does not 0"
  if age < 0:
    raise ValueError("age does not under 0")
  elif age < 18:
    raise Exception("you are under 18")
  else:
    print("congratulations you ar approved for vote")
  
try:
  user_age = int(input("Enter Your Age: "))
  check_age(user_age)

except AssertionError as error:
  print(f"invalid input: {error}")

except ValueError as error:
  print(f"input error: {error}")

except Exception as error:
  print(f"worning! {error}")

else:
  print("everything all okay")

finally:
  print("Pogram process finished")