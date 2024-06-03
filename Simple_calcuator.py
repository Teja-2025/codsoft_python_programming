# Arthimetic_calcuator is a class,which consists of 4 methods named as add(),subract(),multiply(),div().
# add() method is for addition of two numbers.
# subract() method is for subraction of two numbers.
# multiply() method is for multiplication of two numbers.
# div() method is for division.

class Arthimetic_calcuator :

    def __init__(self):
          self.result=0


    def add(self,number1,number2) :
          self.result=number1+number2
          print(f"Addition of {number1} and {number2} is : {self.result}")


    def subract(self,number1,number2) :
            self.result=number1-number2
            print(f"Subraction of {number1} and {number2} is : {self.result}")

    def multiply(self,number1,number2):
          self.result=number1 * number2
          print(f"Multiplication of {number1} and {number2} is : {self.result}")


    def div(self,number1,number2) :
               
               try:
                    self.result=number1/number2  
                    print(f"Division of {number1} by {number2} : {self.result}")
                    

               except ZeroDivisionError :
                    print("Error")
                    
          

def main() :
     
     calcuator=Arthimetic_calcuator()
     Number1=eval(input("Enter a number : "))
     Number2=eval(input("Enter a number : "))
     print(" *******Arthimetic operations******** ")
     print("\t 1.Addition \t")
     print("\t 2.Subraction \t")
     print("\t 3.Multiplication \t")
     print("\t 4.Division \t")
     choice=int(input("Enter your choice : "))
     if choice==1 :
        calcuator.add(Number1,Number2)  
     elif choice==2 :
          calcuator.subract(Number1,Number2)
     elif choice==3 :
        calcuator.multiply(Number1,Number2)  
     elif choice==4 :
         calcuator.div(Number1,Number2)
     else:
         print("Enter valid choice",end="\n")
         return main()

main()
   
