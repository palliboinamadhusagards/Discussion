from Elderprofile import  Elder

class Younger(Elder):
    younger_list = []

    @classmethod
    def add_younger(cls, younger):
        cls.younger_list.append(younger)
    
    @classmethod
    def get_younger(cls, name):
        for younger in cls.younger_list:
            if younger.name == name:
                return younger
          
    def __init__(self,name,mobile,email, password,current_balance):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.password = password
        self.current_balance = current_balance
        self.youngercount = []
        self.review = {}
        self.rating = {}
        
        Younger.add_younger(self)
        
    def login(self, email, password):
        if email == self.email and password == self.password:
            return "Login Successfully"
        else:
            return "Enter username and password not valid try again"
        
    def younger_dashboard(self):
        eldercount = len(self.youngercount)
        print("Currently you are taking care of {eldercount} Elders, You can request for 4-{eldercount} elders.\n 1.Request Elder\n2.Reviews and Ratings\n3.Log out".format(eldercount = eldercount))
        print(" "*50)
        choice = int(input())
        
        if choice == 1:
            self.request_elder()
            
        if choice == 2:
            self.elder_reviewrating()
                            
        if choice == 6:
            self.logout()
                
    def request_elder(self):
        eldercount = len(self.youngercount)
               
        if eldercount <= 4:
            request = input("Enter Elder name whom you want to take care:")
           
            if request in Elder.true_elderlist:
                print("Your request is been accepted and under process...")
                print(" "*50)
                elder = Elder.get_elder(request)
                if request not in self.youngercount:
                    elder.accept_request(self.name)
                    if elder.get_approvestatus() == True:
                        self.youngercount.append(request)
                    else:
                        print("Sorry your request is not approved by elder '{}'".format(elder.name))
                else:
                    print("For the elder {} request is already approved".format(request))
            else:
                print("Invalid option, please select from above choices")
                elder.elder_dashboard()
        else:
            print("You are already taking care of 4 elders. So, you are not eligile to send another request")
        
#         self.younger_dashboard()
            
    def elder_reviewrating(self):
        print("Kindly provide your review and rating for the elder whom you taken care of...")
        print(" "*50)
        review_id = input("Enter Elder ID:")
        elder = Elder.get_elder(review_id)
        
        if elder:
            review_user = input("Provide your review:")
            rating_user = int(input("Provide rating for user on a scale of 1 to 5:"))
            
            if self.review.get(review_id):  #will get value if present else none
                self.review.get(review_id).append(review_user)
                self.rating.get(review_id).append(rating_user)
            else:
                self.review.setdefault(review_id, [review_user])
                self.rating.setdefault(review_id, [rating_user])
            
            avg_rating = sum(self.rating[review_id]) / len(self.rating[review_id])
            print(self.review[review_id], self.rating[review_id])
            print(" "*50)
            print("Average rating for elder '{}' : {}".format(elder.name, avg_rating))
            
        else:
            print("Invalid review id")
      
        
    def get_elderlist(self):
        eld_list = self.youngercount
        return eld_list
    
    def get_youngerdetails(self):
        return self.name
