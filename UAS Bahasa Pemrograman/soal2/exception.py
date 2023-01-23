#try-except
print("1. TRY-EXCEPT")
try:
  print(x)
except:
  print("An exception occurred")
print("")

#try-except-except
print("2. TRY-EXCEPT-EXCEPT")
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
print("")

#try-except-else
print("3. TRY-EXCEPT-ELSE")
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
print("")

#try-except-finally
print("4. TRY-EXCEPT-EXCEPT-FINALLY")
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")