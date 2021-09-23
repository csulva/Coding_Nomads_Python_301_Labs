# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

class PrinceException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
    def __str__(self):
        print('I have found you, Prince!')

with open('books/crime_and_punishment.txt', 'r') as fin:
    crime = fin.read()

with open('books/pride_and_prejudice.txt', 'r') as fin:
    pride = fin.read()

with open('books/war_and_peace.txt', 'r') as fin:
    war = fin.read()

books = [crime, pride, war]

for book in books:
    if "Prince" in book[0:101]:
        raise PrinceException('AHa!')
