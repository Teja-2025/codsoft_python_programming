# password_gererator is a class,which consists of 3 methods named as simple_password,medium_password and complex_password.
# simple_password() method is gererate simple password,which consists only alphabets.
# medium_password() method is generate medium level password,which consists alphanumeric characters.
#complex_password() method is generate complex level password,which consists symbools and alphanumeric.
# main() method is for access to this class.




from random import *

class password_generator:
   def __init__(self):
      self.password=""
   def simple_password(self,length):
        #print("In simple password , password only consists of upper and lower case characters")
        upper_case=int(input("enter how many  uppercase characters do you want to present in your password : "))
        lower_case=int(input("enter how many  lowercase characters do you want to present in your password : "))
        if (upper_case + lower_case) == length :
          for i in range(upper_case):
            self.password +=chr(randint(65,90))
          for i in range(lower_case):
            self.password +=chr(randint(97,122))
          print(f"Your password : {self.password}")
        else :
          print("**sum of uppercase and lowercase length must be equal to password length**")
   def medium_password(self,length):
        #print("In Medium level password , password consists of upper and lower case characters,numbers")
        upper_case=int(input("enter how many  uppercase characters do you want to present in your password :  "))
        lower_case=int(input("enter how many  lowercase characters do you want to present in your password :  "))
        numbers=int(input("enter how many  numbers do you want to present in your password :  "))
        if (upper_case + lower_case + numbers) == length :
          for i in range(upper_case):
            self.password += chr(randint(65,90))
          for i in range(numbers):
            self.password += str(randint(0,9))
          for i in range(lower_case):
            self.password += chr(randint(97,122))
          print(f"Your password : {self.password}")
        else :
         print("**sum of uppercase ,lowercase and numbers length must be equal to password length** ")
   def complex_password(self,length):
        #print("In Complex level password , password consists of all symbools,characters and numbers")
        for i in range(length):
           self.password +=chr(randint(48,123))
        print(f"Your password : {self.password}")

def main():
  
   password=password_generator()
   length=int(input("Enter length of the password : "))
   if length < 0 :
      print("password length must be positive")
      return main()
   print(" Complexity levels of password :" ,end="\n")
   print("\t1.Simple\t")
   print("\t2.Medium\t")
   print("\t3.Complex\t")
   choice=int(input("Enter your choice : "))
   if choice==1 :
      password.simple_password(length)
   elif choice==2:
      password.medium_password(length)
   elif choice==3:
      password.complex_password(length)
   else:
      print("Enter valid choice",end="\n")
      return main()
main()


      
      
   





