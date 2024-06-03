class list_of_tasks :
    def __init__(self):
        self.list_of_actions=[]

    def create_task(self) :
        add=str(input(" \n Enter task : "))
        self.list_of_actions.append(add)
        print(" \n your task is inserted \n")

    def update_task(self):
        index=int(input(" \nEnter index number, where you want to update ? : "))
        if index > len(self.list_of_actions):
            print(" \n It's out of list bound \n ")
            return False
        else:    
            task=str(input(" \nEnter your update task : "))
            self.list_of_actions[index]=task
            print("  \n your list is updated \n")

    def display_task(self):
        if len(self.list_of_actions)>0:
            print(f"list of actions : {self.list_of_actions}")
        else:
            print("\n  Your list is empty \n")
            return False

    def track_task(self):
        index=int(input("Enter index at which task is completed : "))
        if index > len(self.list_of_actions):
            print(" \n No tasks at that index \n ")
            
        else:
            print(f"{self.list_of_actions[index]} task is completed ")
            del self.list_of_actions[index]

        


def main():

    tasks=list_of_tasks()
    while True:
        print("\t 1.Create task")
        print("\t 2.Update task")
        print("\t 3.Display tasks")
        print("\t 4.Track task")
        choice=int(input("Enter your choice : "))
        if choice==1 :
            tasks.create_task()
        elif choice==2 :
            tasks.update_task()
        elif choice==3 :
            tasks.display_task()
        elif choice==4 :
            tasks.track_task()
        else :
            print("  -----exiting-----")
            return False


main()