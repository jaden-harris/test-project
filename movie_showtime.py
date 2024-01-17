movie_times = {
    'Top Gun': '20:00',
    'Forrest Gump': '18:00',
    'Ted': '21:00',
    'Titanic': '19:00'
}

print("Here are the movies that are currently showing:")

for key in movie_times:
    print(key)

movie = input("What movie would you like the time for?\n")
movie_wanted = movie_times.get(movie)
if movie_wanted:
    print(movie_wanted)
else:
    print("Movie does not exist!")



