class Library :

    Author  = []
    Book    = []
    Admin   = []

    # **************  method to change password *******************************
    def new_pass(self , id , old_pass):
        admin = self.Admin[id]
        if admin.Password == old_pass :
            print("enter new password : ") ; new_pass = input()
            admin.set_user_pass(admin.User_name , new_pass)
        else:
            print("your password is wrong.")

    # **************  method to edit Profile *******************************

    def edit_profil(self , id ):
        id = id - 1
        admin = self.Admin[id]
        print("name", admin.name, "  Phone", admin.Phone, "  Email", admin.Email, "address", admin.address)
        print("enter new name : ")    ; name    = input()
        print("enter new Phone : ")   ; Phone   = input()
        print("enter new Email : ")   ; Email   = input()
        print("enter new address : ") ; address = input()
        admin = self.Admin[id]
        if name !="" and name != "\n" :
            admin.name = name
        if Phone !="" and Phone != "\n" :
            admin.Phone = Phone
        if Email !="" and Email != "\n" :
            admin.Email = Email
        if address !="" and address != "\n" :
            admin.address = address

    # **************  method to add new Admin *******************************

    def add_admin(self, Admin):
        state = 1
        while state :
            print("enter new user name : ") ; userName = input()
            print("enter new password : ") ; pas = input()
            for admin in self.Admin :
                if admin.User_name == userName :
                    print("this user_name exist before please try again :")
            else:
                state = 0
        else:
            self.Admin.append(Admin)
            admin = self.Admin[-1]
            admin.set_user_pass(userName ,pas )

    # **************  Log in  *******************************

    def Log_in(self):
        try_again = 3
        done_user_name = 0
        password = ""
        permission =""
        id = ""
        while try_again != 0 and done_user_name == 0:
            print("Enter your user_name : ")
            user_name = input()
            for admin in self.Admin:
                if user_name == admin.user_name:
                    password   = admin.Password
                    permission = admin.get_permission()
                    id = admin.id
                    done_user_name = 1
                    break
            else:
                print("user_name is wrong .")
                try_again -= 1
        else:
            if done_user_name == 0:
                print("good bay")
                return 0

        while try_again != 0 :
            print("Enter your Password : ")
            password_check = input()
            if password_check == password:
                print("welcome")
                return permission , id
            else:
                print("your password is wrong .")
                try_again -= 1
        else:
                print("good bay")
                return 0
        return 0

    #**************  method to add new author *******************************

    def add_author(self , author):
        self.Author.append(author)

    # **************  method to remove author *******************************

    def remove_author(self , id ):

        for author in self.Author:
            if author.id == id:
                self.Author.remove(author)
                return

        print("Author with id", id, "is not found!")

    # **************  method to print author *******************************

    def print_author(self , id ):

        for author in self.Author:
            if author.id == id:
                print("Name  : ", author.name , "Phone : ", author.phone , "Email : ", author.Email)
                return

        print("Author with id", id, "is not found!")

    # **************  method to print authors *******************************

    def print_authors(self ):
        for author in self.Author :
            print(author.id,") ","name : ",author.name , "  phone : " , author.phone,"  Email : ",author.Email)

    # **************  method to print books of this author *******************************

    def print_author_books(self , id):
        is_author_exist = False
        author_name = ""
        for author in self.Author :
            if author.id == id :
                is_author_exist = True
                author_name = author.name
                break

        if is_author_exist == False :
            print("Author with id : ",id ,"is not found")
            return

        print("books of author" ,author_name , " : ")
        for book in self.Book :
            if book.id_author == id :
                print("title : " , book.title)

    # **************  method to ADD Book *******************************

    def add_book(self, book):
        self.Book.append(book)

    # **************  method to Remove Book *******************************

    def remove_book(self, id):
        for book in self.Book:
            if book.id == id:
                self.Book.remove(book)
                return
        print("Book with id", id, "is not found!")

    # **************  method to print Book *******************************

    def print_book(self, id):
        for book in self.Book:
            if book.id == id:
                print("Book with id", id, " information .")
                print("Title : ", book.title)
                print("Publishing date : ", book.publishing_date)
                for author in self.Author :
                    if author.id == book.id_author :
                        print("Author : " , author.name )
                        return

                return
        print("Book with id", id, "is not found!")

    # **************  method to print Books *******************************

    def print_books(self):
        for book in self.Book:
            print("Book with id", book.id, " info.")
            print("Title:", book.title)
            print("Publishing date:", book.publishing_date)
            for author in self.Author:
                if author.id == book.id_author:
                    print("Author : ", author.name)
                    break
            print("-------------------------------------")