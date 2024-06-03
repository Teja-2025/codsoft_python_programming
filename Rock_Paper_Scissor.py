# Here,Rock_paper_scissor is a class,which consists of two methods named as user_choice and computer_choice and one constructor.
# user_choice() method is for read the user choice.
# computer_choice() method is for read the computer choice.
# There is a method named as winner(),which is for deciding the winner based on their choice.
# instructions() method is for display the game instructions.
# main() method is for call the methods which are in Rock_paper_scissor class.


from random import *
class Rock_paper_scissor :
    
    def __init__(self) :
        self.user=0
        self.computer=0

    def user_choice(self):
        print("\n 1.Rock \n 2.Paper \n 3.Scissor \n")
        self.user=int(input("Enter your choice : "))
        return self.user
    
    def computer_choice(self) :
        self.computer=randint(1,3)
        print(f"\n computer choose : {self.computer} ")
        return  self.computer
        
        
def winner(user,computer) :
         print(user,computer)
         if user==computer:
              
              print(" \t --- Tie game ---\t")
              
         elif ((user==1 and computer==3) or (user==2 and computer==1) or (user==3  and computer==2) ):
               
               print("  \t  ***  you win  *** \t  \n")
               print("\t \t  congrulations  \t \t \t")
         else:
                print("  \t  ***  computer win  *** \t  \n")
                print("\t \t  congrulations  \t \t \t")


def instructions():
        print(" \n \t  \t \t \t INSTRUCTIONS \t \n")
        print(" \t ~ If you choose rock,you will win aganist scissors but lose aganist paper \t")
        print(" \t ~ If you choose paper ,you will win aganist rock but lose aganist scissors  \t")
        print("\t  ~ If you choose scissors ,you will win aganist paper but lose aganist rock \t \n")
        print("  \t  \t  \t ******Let's begin the game********** \t \n")


def main() :
    
    playgame=Rock_paper_scissor()
    user=playgame.user_choice()
    if (user <= 0) or (user > 3) :
            print("Enter valid choice\n ")
            main()
    computer=playgame.computer_choice()
    winner(user,computer)
    print("\n")
    choice=eval(input("Do you want to play again ? (Enter(1-yes Or 0-no)):"))
    if choice==1:
         main()
    else:
         print("  \t  \t Thank you  \t   \n \t \t ----GAME OVER---- \t")

instructions() #it calls instructions method
main()         #it calls main method