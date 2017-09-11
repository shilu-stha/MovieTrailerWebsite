import fresh_tomatoes
import media
import requests
import json

# Make a get request to get the list of latest movies from the Movie Db api.
response = requests.get("https://api.themoviedb.org/4/list/33436?api_key=e636464b21df7ea6ab6b26b273fea8bc")

# Get the json response returned from the api call.
response_data = response.json()

# Print the status code of the response. For test only.
print(response.status_code)

# Start an empty list
list = []          

# Loop through each response results to get all the list of movies and add it in a list
# according to our Movie model class.
for db_movie in response_data["results"]:

    # get image url from movie db using movies's poster path
    image_url = "https://image.tmdb.org/t/p/w500/"+db_movie["poster_path"]

    # get youtube key from a different api of movie db and then create a final complete youtube url
    trailer_url = "https://api.themoviedb.org/3/movie/"+str(db_movie["id"])+"/videos?api_key=e636464b21df7ea6ab6b26b273fea8bc&language=en-US"
    trailer_response = requests.get(trailer_url)
    trailer_data = trailer_response.json()["results"]
    youtube_url = "https://www.youtube.com/watch?v="+trailer_data[0]["key"]

    # Create Movie object    
    movie = media.Movie(db_movie["title"],
                        db_movie["overview"],
                        image_url,
                        youtube_url)

    # Use append() to add elements
    list.append(movie)   
 
fresh_tomatoes.open_movies_page(list)
