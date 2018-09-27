a = input("ENter any text")

a = a.lower()

b = reversed(a)


if list(a) == list(b):
   print("It is palindrome")
else:
   print("It is not palindrome")