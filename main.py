# 1.1 Implemens a function to calculate a factorial.
def fact_rec(n):
  if n==0 or n==1:
     return 1
  else:
    return n*fact_rec(n-1)
number=4
result=fact_rec(number)
print("The factorial of 4 is",result)