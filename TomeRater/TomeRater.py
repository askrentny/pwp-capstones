class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The user's email has been updated to " + address + ".")
    
    def read_book(self, book, rating=None):
        self.books[book] = rating
    
    def get_average_rating(self):
        rating_total = 0
        rating_count = 0
        for rating in self.books.values():
            if rating != None:
                rating_total += rating
                rating_count += 1
        if rating_count == 0:
            return 0
        else:
            return rating_total / rating_count

    def __repr__(self):
        book_rating_list = "\n"
        for book, rating in self.books.items():
            book_rating_list += "Book: " + str(book) + " (Rating: " + str(rating) + ")\n"
        return "User: " + self.name + "\nEmail: " + self.email + "\nBooks Read: " + str(len(self.books)) + "\nAvg Rating: " + str(self.get_average_rating()) + book_rating_list

    def __eq__(self, other_user):
        if (self.name is other_user.name) and (self.email is other_user.email):
            return True
    
        elif type(self) != type(other_user):
            return False
        
        else:
            return self.name == other_user.name

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn
    
    def get_ratings(self):
        for r in self.ratings:
            print(r)
        return self.title + " has " + str(len(self.ratings)) + " rating(s)."

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print(self.title + "'s isbn has been updated to " + str(new_isbn) + ".")

    def add_rating(self, rating):
        if isinstance(rating, int) == True:
            if (rating >= 0 and rating <=4):
                self.ratings.append(rating)
        else:
            print("Invalid rating")

    def get_average_rating(self):
        avg_rating = 0
        for rating in self.ratings:
            avg_rating += rating
        if len(self.ratings) == 0:
            return 0
        else:
            return avg_rating / len(self.ratings)

    def __repr__(self):
        return self.title + " (ISBN: " + str(self.isbn) + ")"

    def __eq__(self, other_book):
        if type(self) != type(other_book):
            return False
        elif (self.title == other_book.title) and (self.isbn == other_book.isbn):
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject + " (ISBN: " + str(self.isbn) + ")"

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return self.title + " by " + self.author + " (ISBN: " + str(self.isbn) + ")"



class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        self.books[new_book] = 0
        return new_book

    def create_novel(self, title, author, isbn):
        new_novel = Fiction(title, author, isbn)
        self.books[new_novel] = 0
        return new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        self.books[new_non_fiction] = 0
        return new_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1
            elif book in self.books:
                self.books[book] += 1
        else:
            print("No user with email " + email + "!")

    def add_user(self, name, email, user_books=None):
        if email in self.users.keys():
            print("The user with email address " + email + " already exists.")
        elif ("@" in email) and ((".com" in email) or (".edu" in email) or (".org" in email)):
            new_user = User(name, email)
            self.users[email] = new_user
            if user_books:
                for book in user_books:
                    TomeRater.add_book_to_user(self, book, email)
        else:
            print("Not a valid email address for " + name + ".")
            

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        read_value = 0
        read_book = []
        for book in self.books:
            if self.books[book] > read_value:
                read_value = self.books[book]
                read_book = book
        return read_book

    def highest_rated_book(self):
        highest_rating = 0
        highest_book = []
        for book in self.books:
            book_avg = book.get_average_rating()
            if book_avg > highest_rating:
                highest_rating = book_avg
                highest_book = book
        return highest_book

    def most_positive_user(self):
        positive_user_avg = 0
        positive_user = []
        for user in self.users.values():
            user_avg = user.get_average_rating()
            if user_avg > positive_user_avg:
                positive_user_avg = user_avg
                positive_user = user
        return positive_user

    def __repr__(self):
        return "TomeRater has " + str(len(self.users)) + " user(s) and " + str(len(self.books)) + " book(s) in the catalog."
    
    def __eq__(self, other_tome_rater):
        if type(self) != type(other_tome_rater):
            return False
        elif (self.users == other_tome_rater.users) and (self.books == other_tome_rater.books):
            return True
        else:
            return False










