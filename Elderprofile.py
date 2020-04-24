# from Youngerprofile import  Younger

class Elder:
    
    true_elderlist = []
    
    elder_list = []
    
    @classmethod
    def addElder(cls, elder):
        cls.elder_list.append(elder)
        
    @classmethod
    def get_elder(cls, name):
        for elder in cls.elder_list:
            if elder.name == name:
                return elder
    
    @classmethod
    def truestatuslist(cls,obj):
        if obj.status:
            if obj.name not in cls.true_elderlist: 
                cls.true_elderlist.append(obj.name)
        else:
            pass
    
    def __init__(self,name,email, password,current_balance):
        self.name = name
        self.email = email
        self.password = password
        self.status = ""
        self.current_balance = current_balance
        self.amount = 0
        self.approve = False
        self.youngername = ""
        self.review = {}
        self.rating = {}
        
        Elder.addElder(self)
        
    
    def login(self, email, password):
        if self.email == email and self.password == password:
            return "Login Successfully"
        else:
            return "Enter username and password not valid try again"
        
    def elder_dashboard(self):
        if self.status == 1:
            print(" "*50)
            print("You are currently available to take care of.\n 1.Status_change\n2.Pay for younger\n3.Younger details\n4.Reviews and Ratings\n5.Log out")
            print(" "*50)
            choice = int(input())
            if choice == 1:
                self.status_change()
            
            elif choice == 2:
                self.pay_younger()
                 
            elif choice == 3:
                self.younger_details()
                            
            elif choice == 4:
                self.younger_reviewratings()
            
            elif choice == 5:
                self.logout()
        
        else:
            print("You are currently unavailable to take care of.\n 1.Change status \n2.Log out")
            print(" "*50)
            choice = int(input())
            if choice == 1:
                self.status_change()
          
            elif choice == 2:
                self.logout()
            
    def status_change(self):
        choice = int(input("Enter your status:\n 1. Availabe \n 2. Unavilable \nEnter your option"))
        print(" "*50)
        if choice == 1:
            self.status = True
            Elder.truestatuslist(self)
        
        elif choice == 2:
            self.status = False
        
        print("Status changed")

        self.elder_dashboard()
        
    def get_elderstatus(self):
         return self.status
        
    def get_approvestatus(self):
        return self.approve
    
          
    def pay_younger(self):
        amount = int(input("Enter fee amount for younger:"))
        self.amount = amount
        balance = self.current_balance - self.amount
        
        younger = Younger.get_younger(self.youngername)
        print(" "*50)
        younger.current_balance += amount
        print(" "*50)
        print("Elder {} paid fee {} for the younger {} who take care.The remaining balance is {}.".format(self.name,self.amount,self.youngername,balance))
        print(" "*50)
        print("Younger {} available balance is {}".format(self.youngername, younger.current_balance))
        print(" "*50)
        
        
    def accept_request(self, name):
        approve = ""
        print(f"Younger person {name} is requesting for approval")
        choice = int(input("Enter your status:\n 1. Approve \n 2. Not Approve \n 3. Enter your option"))
        if choice == 1:
            self.approve = True
            self.youngername = name
            print("Approve")
        elif choice == 2:
            self.approve = False
            print("Not approve")
            
#         self.elder_dashboard()
                     
    def younger_details(self):
        younger = Younger.get_younger(self.youngername)
        print("View who is taking care of Elder {} :\n".format(self.name))
        print(" "*50)
        print("Younger details:\nYounger name: {}, Younger mobile: {}".format(younger.name, younger.mobile))
    
    def younger_reviewratings(self):
        print("Kindly provide your review and rating for the younger {} who provide care of...".format(self.youngername))
        younger = Younger.get_younger(self.youngername)
        if younger:
            review_user = input("Provide your review:")
            rating_user = int(input("Provide rating for user on a scale of 1 to 5:"))
            
            if self.review.get(self.youngername):  #will get value if present else none
                self.review.get(self.youngername).append(review_user)
                self.rating.get(self.youngername).append(rating_user)
            else:
                self.review.setdefault(self.youngername, [review_user])
                self.rating.setdefault(self.youngername, [rating_user])
            
            print(self.review[self.youngername], self.rating[self.youngername])
            
        else:
            print("Invalid review id")
           
    def logout(self):
        return False