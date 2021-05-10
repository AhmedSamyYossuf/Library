from Author import Author
from Book import Book
from Library import Library
from Admin import Owner , Seller

lib =Library()

admin = Owner("ahmed" , "5656121" , "ahmed.com" , "Helwan - Egypt")
lib.add_admin(admin)

"""
admin = Owner("ahmed" , "5656121" , "ahmed.com" , "Helwan - Egypt")
admin.set_user_pass("ahmed","123")
lib.add_admin(admin)
"""

permission , id = lib.Log_in()

while permission != 0 and permission != "" :

    #******************** page for Owner ************************************

    if permission == "Owner" :
        print("please enter number : ")    ; print("1)  to add a new admin ") ; print("2)  to add a new Author ")
        print("3)  to add a new Book ")    ; print("4)  to remove author ")   ; print("5)  to remove book  ")
        print("6)  to print one author ")  ; print("7)  to print authors ")   ; print("8)  to print one book ")
        print("9)  to print books ")       ; print("10) to print books of this author ")
        print("11) to edit your profile ") ; print("12) to exit ")
        choose = input()

        #**************************** Add new admin ****************************************
        if   choose == "1" :
            print("enter name")
            name = input()
            print("enter permission")
            perm = input()
            new_admin = ""
            if perm == "Owner" :
                new_admin  = Owner(name , "" , "" , "")
            elif perm == "Seller" :
                new_admin = Seller(name, "", "", "")

            lib.add_admin(new_admin)
        #**************************** add a new author ******************************
        elif choose == "2" :
            print("enter name")  ; name = input()
            print("enter Phone") ; Phone = input()
            print("enter Email") ; Email = input()
            new_author = Author(name , Phone , Email)
            lib.add_author(new_author)

        # **************************** add a new Book ******************************
        elif choose == "3" :
            print("enter book title ")        ; title = input()
            print("enter publishing_date ")   ; publishing_date = input()
            print("enter version" )           ; version = input()
            print("choose number of author ") ; lib.print_authors()
            print("enter number is : ") ; id_author = input()

            new_book = Book(title , publishing_date , version , id_author)
            lib.add_book(new_book)

        # **************************** add remove author ******************************
        elif choose == "4" :
            print("choose number of author ") ; lib.print_authors()
            print("enter number is : ")       ; id_author = input()
            lib.remove_author(int(id_author))
        # **************************** remove Book ******************************
        elif choose == "5" :
            print("choose number of Book ") ; lib.print_books()
            print("enter number is : ")     ; id_book = input()
            lib.remove_book(int(id_book))

        # **************************** print one author ******************************
        elif choose == "6" :
            pass
        # **************************** print authors ******************************
        elif choose == "7" :
            lib.print_authors()
        # **************************** print one Book ******************************
        elif choose == "8" :
            pass
        # **************************** print Books ******************************
        elif choose == "9" :
            lib.print_books()
        # **************************** print books of this author ******************************
        elif choose == "10":
            print("choose number of author ") ; lib.print_authors()
            print("enter number is : ")       ; id_author = input()
            lib.print_author_books(int(id_author))
        # **************************** edit your profile ******************************
        elif choose == "11":
            print("choose 1)for edit profile \n2)for change password")
            ch = input()
            if ch == "1" :
                lib.edit_profil(id)
            elif ch == "2" :
                print("please enter your password") ; pas = input()
                lib.new_pass(id , pas)
            else:
                print("wrong choose")
        # **************************** exit ******************************
        elif choose == "12":
            print("Good bay")
            break
    # ******************** page for Owner ************************************
    elif permission == "Seller" :
        print("please enter number : ")    ; print("1)  to remove book  ")
        print("2)  to print one author ")  ; print("3)  to print authors ")     ; print("4)  to print one book ")
        print("5)  to print books ")       ; print("6) to print books of this author ")
        print("7) to edit your profile ") ; print("8) to exit ")
        choose = input()

        # **************************** remove Book ******************************
        if choose == "1":
            print("choose number of Book ");
            lib.print_books()
            print("enter number is : ");
            id_book = input()
            lib.remove_book(int(id_book))

        # **************************** print one author ******************************
        elif choose == "2":
            pass
        # **************************** print authors ******************************
        elif choose == "3":
            lib.print_authors()
        # **************************** print one Book ******************************
        elif choose == "4":
            pass
        # **************************** print Books ******************************
        elif choose == "5":
            lib.print_books()
        # **************************** print books of this author ******************************
        elif choose == "6":
            print("choose number of author ");
            lib.print_authors()
            print("enter number is : ");
            id_author = input()
            lib.print_author_books(int(id_author))
        # **************************** edit your profile ******************************
        elif choose == "7":
            print("choose 1)for edit profile \n2)for change password")
            ch = input()
            if ch == "1":
                lib.edit_profil(id)
            elif ch == "2":
                print("please enter your password");
                pas = input()
                lib.new_pass(id, pas)
            else:
                print("wrong choose")
        # **************************** exit ******************************
        elif choose == "8":
            print("Good bay")
            break

