class Calculator:
    def __init__(self):
      self.history=[]

    def add(self,a,b):
        ans=a+b
        self.history.append(f"{a}+{b}={ans}")
        return ans
    def subtract(self,a,b):
       ans=a-b
       self.history.append(f"{a}-{b}={ans}")
       return ans
    def multiply(self,a,b):
       ans=a*b
       self.history.append(f"{a}*{b}={ans}")
       return ans
    def division(self,a,b):
       try:
        ans=a/b
        self.history.append(f"{a}/{b}={ans}")
        return ans
       except ZeroDivisionError:
          return "Error!"
    def view_history(self):
       if not self.history:
          return "empty"
       return "\n".join(self.history)
       
    def clear_history(self):
       self.history=[]
       return "Cleared successfully!"

def main():
    a=float(input("Please Enter the first number:"))
    b=float(input("Please Enter the second number:"))
    operand=input("+,-,/,*:")    

    my_calc=Calculator()  
    if operand=="+":
        print(my_calc.add(a,b)) 
    elif operand=="-":
        print(my_calc.subtract(a,b))
    elif operand=="*":
        print(my_calc.multiply(a,b)) 
    elif operand=="/":
        print(my_calc.division(a,b))
        

    if input("View history? (yes/no)")=="yes":
     print(my_calc.view_history())


    if input("Clear history? (yes/no)")=="yes":
     my_calc.clear_history()
 

if __name__=="__main__" :
   main()

   
        
