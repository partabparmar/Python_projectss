

class User():
    def __init__(self,Name,AccNo,Gender,Total_Balance):
        self.Name=Name
        self.AccNo=AccNo
        self.Gender=Gender
        self.Total_Balance=Total_Balance

    def User_Detail(self,Acc):
        self.Acc=Acc
        print(
        f"""
        Name:     {self.Name}
        Acc No:   {self.Acc}
        Gender:   { self.Gender}
        Balance:  {self.Total_Balance}
        """)




class Bank(User):
    def __init__(self,Name,AccNo,Gender,Total_Balance):
        super().__init__(Name,AccNo,Gender,Total_Balance)
        


    def add_Balance(self,add_amount):
        self.add_amount=add_amount
        total_balance=self.Total_Balance+self.add_amount
        return total_balance
    

    def Create_Acc(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(f""" detail are ,
        {self.name}
        {self.age}
        {self.gender}""")
        

    def cash_draw(self,cash_amount):
        self.cash_amount=cash_amount
        if self.Total_Balance>self.cash_amount:
           total_balance= self.Total_Balance-self.cash_amount
           return total_balance

        else:
            print("you have not enough to cash _draw")


bank1=User("partab",'xx2415','Male',300)

john=Bank("partab",'xx2415','Male',500)


def people_choice():
    print("How can we help you")
    print("1. Create New Account")
    print("2.Chech the Balance")
    print("3.want a with_draw")
    print("4.want a Add_Balnce ")
    selection=int(input("enter a number      "))
    if selection==1:
        print("Welcome the portal")
        name=input("Tell The name   ")
        age=input("tell the age     ")
        gender=input("tell the gender ")
        john.Create_Acc(name,age,gender)
    

    elif selection==2:
        Acc=input("Tell the ACC NO:      ")
        bank1.User_Detail(Acc)

    elif selection==3:
        cash=int(input("enter a with_draw amount    "))
        print('the ramining balance is',john.cash_draw(cash))
        print("  Thank for using   ")
    
    elif selection==4:
        cash_add=int(input("enter amount"))
        print('New Balance is  :',john.add_Balance(cash_add))












people_choice()







