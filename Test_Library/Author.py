class Author :

    __id_author = 0

    def __init__(self , name , phone , Email):
        Author.__id_author += 1
        self.id    = Author.__id_author
        self.name  = name
        self.phone = phone
        self.Email = Email
