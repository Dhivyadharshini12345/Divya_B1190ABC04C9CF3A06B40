#calculate the factorial of a given number
def rec(n) : 
  if n == 0 or n == 1: 
    return 1
  else:
    return n * rec(n - 1)

number = 6
res = rec(number)
print("The factorial of {} is {}".format(number, res))
