#  Assignment 1: Design Your Own Class! 🏗️
#     - Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
#     - Add attributes and methods to bring the class to life!
#     - Use constructors to initialize each object with unique values.
#     - Add an inheritance layer to explore polymorphism or encapsulation.
class Book:
    """
    A class representing a book with attributes and methods to manage its details.
    """

    def __init__(self, title, author, genre, year_published):
        """
        Initializes a new Book instance.

        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        genre (str): The genre of the book.
        year_published (int): The year the book was published.
        """
        self.title = title
        self.author = author
        self.genre = genre
        self.year_published = year_published

    def get_summary(self):
        """
        Returns a summary of the book's details.

        Returns:
        str: A formatted string containing the book's details.
        """
        return f"'{self.title}' by {self.author}, Genre: {self.genre}, Published in {self.year_published}"

    def is_classic(self):
        """
        Determines if the book is considered a classic (published over 50 years ago).

        Returns:
        bool: True if the book is a classic, False otherwise.
        """
        current_year = 2024
        return (current_year - self.year_published) > 50
# Example usage:
if __name__ == "__main__":
    book1 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960)
    book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 2000)

    print(book1.get_summary())
    print(f"Is '{book1.title}' a classic? {'Yes' if book1.is_classic() else 'No'}")

    print(book2.get_summary())
    print(f"Is '{book2.title}' a classic? {'Yes' if book2.is_classic() else 'No'}")




#  Activity 2: Polymorphism Challenge! 🎭
#    - Create a program that includes animals or vehicles with the same action (like move()). However, make each class define 
#     move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Vehicle:
    """
    A base class representing a generic vehicle.
    """

    def move(self):
        """
        A method to be overridden by subclasses to define how the vehicle moves.
        """
        raise NotImplementedError("Subclasses must implement this method")  
class Car(Vehicle):
    """
    A class representing a car, inheriting from Vehicle.
    """

    def move(self):
        """
        Defines how a car moves.
        """
        return "Driving 🚗  "
class Plane(Vehicle):
    """
    A class representing a plane, inheriting from Vehicle.
    """

    def move(self):
        """
        Defines how a plane moves.
        """
        return "Flying ✈️  "
# Example usage:
if __name__ == "__main__":
    my_car = Car()
    my_plane = Plane()

    print(my_car.move())
    print(my_plane.move())  

