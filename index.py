
from Elderprofile import  Elder
from Youngerprofile import  Younger

ed1 = Elder("abc","abc@xyz.com", 123,10000)
ed2 = Elder("pqr","pqr@xyz.com", 132,25000)
ed3 = Elder("klm","klm@xyz.com", 123,10000)
ed4 = Elder("uvw","uvw@xyz.com", 132,25000)
ed5 = Elder("efg","efg@xyz.com", 123,10000)
ed6 = Elder("hij","hij@xyz.com", 132,25000)


yng1 = Younger("stu",9933366677,"stu@xyz.com", 321,0)
yng2 = Younger("klm",9955566677,"klm@xyz.com", 232,0)



# class main(Elder,Younger):

def index():
    print("-"*86)
    print("*****************************CARE-ALL PROJECT Index***********************************")
    print("-"*86)

    print("Please select your option\n1.Login as Elder\n2.Login as Younger\n3.exit()")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        user_id = input("Enter elder user id: ")
        email = input("Enter elder email id: ")
        password = input("Enter password: ")
        
        elder = Elder.get_elder(user_id)
        
        
        if elder.email == email and elder.password == password:
            elder.login(elder.email, elder.password)
            print("Elder '{}' login successfully".format(elder.name))
        else:
            print("Enter username and password not valid try again")
        
        index()
        
    elif choice == 2:
        user_id = input("Enter younger user id: ")
        email = input("Enter younger email id: ")
        password = input("Enter password: ")
        
        younger = Younger.get_younger(user_id)
        if younger.email == email and younger.password == password:
            younger.login(younger.email, younger.password)
            print("Younger '{}' login successfully".format(younger.name))
        else:
            print("Enter username and password not valid try again")
        
        index()
        
    elif choice == 3:
        exit()
 
index()