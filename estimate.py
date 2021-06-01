def wallis(num):
  pi = 1
  for x in range(1,num):
      pi=pi*((4*x**2)/((4*x**2)-1))
  print("Value of pi is:",pi*2)
  return pi


while True:  
  n = int(input("Enter the number of iterations:"))  
  r = wallis(n)
  
    
        
