import webbrowser


class Movie():
    # A model class that holds and encapsulates the data
    # elements of movies being used in the program

    # _ defines that the function is a reserved funtion
    # self: create a instance, itself
    def __init__(self, movie_title,
                 movie_storyline, poster_image, trailer_youtube):
        # Constructor of the class Movie which passes required
        # fields as parameters and sets them in the variable
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # We are using default webbrowser package which
        # opens the given url link
        webbrowser.open(self.trailer_youtube_url)
