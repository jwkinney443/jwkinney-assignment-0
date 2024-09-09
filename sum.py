
def add_numbers(a, b):
  return a + b

if __name__ == "__main__":
  a = float(input("Enter the first number: "))
  b = float(input("Enter the second number: "))

  sum = add_numbers(a,b)
  print("The sum of ", a, " and ", b, " is ", sum)
