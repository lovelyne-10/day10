from replit import clear
import art
print(art.logo)
def addition(n1,n2):
   add=n1+n2
   return add
def substraction(n1,n2):
   sub=n1-n2
   return sub
def multiply(n1,n2):
   mul=n1*n2
   return mul
def divides(n1,n2):
    div=n1/n2
    return div
operator={
  "+": addition,
  "-": substraction,
  "*": multiply,
  "/": divides,
}
def op():
  if con=='+':
    function=operator[con]
    return function(n1,n2)
  elif con=='-':
    function=operator[con]
    return function(n1,n2)
  elif con=='*':
      function=operator[con]
      return function(n1,n2)
  elif con=='/':
      function=operator[con]
      return function(n1,n2)
n1=float(input("Enter the first number:"))
print('''
        +
        -
        /
        *
        ''')
con=input("Enter your operation:")
n2=float(input("Enter the second number:"))
new=op()
print(f"{n1} {con} {n2}= {new}")
x=input("Enter y if  you want to continue and n:")
while True:
  
  if x=='y':
     n1=new
     con=input('Enter a new operation:')
     n2=float(input("Enter another number:"))
     new=op()
     print(f"{n1} {con} {n2}= {new}")
     x=input("Enter y if  you want to continue and n:")
  elif x=='n':
      clear()
  
      

  
