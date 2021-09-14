# CLASSES AND INHERITANCE
# =======================
# 1) Define an empty `Movie()` class.
# 2) Add a dunder init method that takes two arguments `year` and `title`
# 3) Create a sub-class called `RomCom()` that inherits from the `Movie()` class
# 4) Create another sub-class of the `Movie()` class called `ActionMovie()`
#     that overwrites the dunder init method of `Movie()` and adds another
#     instance variable called `pg` that is set by default to the number `13`.
# 5) Practice planning out and flushing out these classes even more.
#     Take notes in your notebook. What other attributes could a `Movie()` class
#     contain? What methods? What should the child classes inherit as-is or overwrite?

class Movie:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating

class RomCom(Movie):
    pass

class ActionMovie(Movie):
    def __init__(self, title, year, rating):
        super().__init__(title, year, rating)
        self.rating = 13

class Horror(Movie):
    def __init__(self, title, year, rating):
        super().__init__(title, year, rating)

    def __str__(self):
        return f'{self.title} ({self.year}) is rated {self.rating}.'


john_wick = ActionMovie('John Wick', 2013, True)

shining = Horror('The Shining', 1980, 'R')

print(john_wick.rating)
print(shining)