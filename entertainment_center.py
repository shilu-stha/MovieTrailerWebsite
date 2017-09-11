import fresh_tomatoes
import media
import requests
# Import the json library
import json

logan = media.Movie("Logan",
                    "American superhero film produced by Marvel Entertainment, TSG Entertainment, and The Donners' Company.",
                    "http://logan-touch.foxfilm.com/backgrounds_logan_outer.jpg",
                    "https://www.youtube.com/watch?v=RH3OxVFvTeg")
despicable_me = media.Movie("Despicable Me 3",
                            "Animation, mischievious minions and Gru",
                            "http://www.susangranger.com/wp-content/uploads/2017/07/yayomg-despicable-me-3.jpg",
                            "https://www.youtube.com/watch?v=6DBi41reeF0")

guardians_of_galaxy = media.Movie("Guardians of the Galaxy Vol. 2",
                                  "American superhero film based on the Marvel Comics superhero team Guardians of the Galaxy",
                                  "http://cdn.movieweb.com/img.site/PHak9S4jdp80cf_1_l.jpg",
                                  "https://www.youtube.com/watch?v=2cv2ueYnKjg")


spiderman = media.Movie("Spider-Man: Homecoming",
                        "American superhero film based on the Marvel Comics character Spider-Man",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_UY1200_CR80,0,630,1200_AL_.jpg",
                        "https://www.youtube.com/watch?v=U0D3AOldjMU")

wonder_woman = media.Movie("Wonder Woman",
                           "Marvel comics, Fantasy Science Fiction",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=1Q8fG0TtVAY")

annabelle = media.Movie("Annabelle: Creation",
                        "A horror movie",
                        "https://1.bp.blogspot.com/-pNM_mtej2RM/WWgpDmpHN4I/AAAAAAAAAE0/2ITrzwQS95U4GgaKzwkilXxGyQ9dIDrDwCLcBGAs/s1600/Annabelle-2-1.jpg",
                        "https://www.youtube.com/watch?v=zjaOgN2Uti8")

# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("https://api.themoviedb.org/4/list/33436?api_key=e636464b21df7ea6ab6b26b273fea8bc")

# Use json.dumps to convert best_food_chains to a string.
response_data = response.json()

# Print the status code of the response.
print(response.status_code)
# print(response_data["results"])

list = []          ## Start as the empty list
  
  
for db_movie in response_data["results"]:
    trailer_response = requests.get("https://api.themoviedb.org/3/movie/"+str(db_movie["id"])+"/videos?api_key=e636464b21df7ea6ab6b26b273fea8bc&language=en-US")
    trailer_data = trailer_response.json()["results"]    
    movie = media.Movie(db_movie["title"],
                        db_movie["overview"],
                        "https://image.tmdb.org/t/p/w500/"+db_movie["poster_path"],
                        "https://www.youtube.com/watch?v="+trailer_data[0]["key"])
    list.append(movie)   ## Use append() to add elements
 
movies = [despicable_me, guardians_of_galaxy, logan, wonder_woman, spiderman, annabelle]
fresh_tomatoes.open_movies_page(list)
