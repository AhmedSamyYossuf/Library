class Admin :

    __id = 0
    user_name = "admin"
    Password  = "admin"
    __Permission = ""

    def __init__(self , name , Phone ,Email , Address):

        self.name   = name
        self.Phone  =Phone
        self.Email  = Email
        self.Address =Address

    def set_user_pass(self , user_name , password):
        self.user_name = user_name
        self.Password  = password

class Owner(Admin) :

    __id = 0
    user_name = "Owner"
    Password =  "Owner"
    __Permission = "Owner"
    def __init__(self ,  name , Phone ,Email , Address):
        super(Owner , self).__init__( name , Phone ,Email , Address)
        Owner.__id += 1
        self.id = Owner.__id

    def get_permission(self):
        return Owner.__Permission

class Seller(Admin) :

    __id = 0
    __Permission ="Seller"
    def __init__(self ,  name , Phone ,Email , Address):
        super(Seller , self).__init__( name , Phone ,Email , Address)
        Seller.__id += 1
        self.id = Seller.__id

    def get_permission(self):
        return Seller.__Permission
