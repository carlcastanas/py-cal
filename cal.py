def add(d, f):
    return d + f

def subtract(d, f):
    return d - f

def multiply(d, f):
    return d * f

def divide(d, f):
    return d / f
    
def modulus(d, f):
    return d % f
    
pro1 = int(input("Enter first number: "))
pro2 = int(input("Enter second number: "))

print("A: Addition")
print("B: Subtraction")
print("C: Multiplication")
print("D: Division")
print("E: Modulus Division")
print("F: Exit")

choice = input("Choose an Operation:")

if choice == 'A':
   print(pro1,"+",pro2,"=", add(pro1,pro2))

elif choice == 'B':
   print(pro1,"-",pro2,"=", subtract(pro1,pro2))

elif choice == 'C':
   print(pro1,"*",pro2,"=", multiply(pro1,pro2))

elif choice == 'D':
   print(pro1,"/",pro2,"=", divide(pro1,pro2))
   
elif choice == 'E':
   print(pro1,"%",pro2,"=", modulus(pro1,pro2))
   
elif choice == 'F':
      print("exit....")
      quit()
else:
   print("Invalid input")
