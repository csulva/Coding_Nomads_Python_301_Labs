# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Artist:
    def __init__(self, artist):
        self.artist = artist

class Album(Artist):
    def __init__(self, name, artist, year, genre, length, songs, own, rating):
        super().__init__(artist)
        self.name = name
        self.year = year
        self.genre = genre
        self.length = length
        self.songs = songs
        self.own = own
        self.rating = rating
    
    def __str__(self):
        return f'{self.name} by {self.artist} is a {self.genre} album that is {self.length} minutes long with {self.songs} songs.\nMy rating: {self.rating}\nOwn it: {self.own}'

    def buy(self):
        self.own = True
    
    def sell(self):
        self.own = False

class Song(Album):
    def __init__(self, name, artist, album, year, genre, length, songs, own, rating):
        super().__init__(name, artist, year, genre, length, songs, own, rating)
        self.songs = 1
        self.album = album
    
    def __str__(self):
        return f'{self.name} is a {self.genre} song by {self.artist} from the {self.album} album that is {self.length} minutes long.\nMy rating: {self.rating}'

pink_floyd = Artist('Pink Floyd')
dark_side = Album('Dark Side of the Moon', f'{pink_floyd.artist}', 1973, 'Progressive Rock', 43.09, 10, True, 10)
meddle = Album('Meddle', f'{pink_floyd.artist}', 1971, 'Progressive Rock', 46.48, 6, False, 10)
time = Song('Time', f'{pink_floyd.artist}', f'{dark_side.name}', 1973, 'Progressive Rock', 6.53, 1, True, 10)

print(dark_side)
print(time)
print(meddle)