file = open("movies.txt")
movies = [movie.strip("\n").split(",") for movie in file]

# print(movies)

# # number of moviews released in 2022
# movie22 = [movie for movie in movies if movie[1] == "2022"]
# print("num of movies in 2022 = ", len(movie22))
#
# # number malayalam movies
# mal_movie = [movie for movie in movies if movie[3] == "malayalam"]
# print("num of malayalam movies= ", len(mal_movie))
#
# # theater released movies
# TheaterReleases = [movie for movie in movies if movie[4] == "theater"]
# print("theater released movies= ", TheaterReleases)
#
# # list of movies whose rating < 5
# RatingAbove5 = [movie for movie in movies if int(movie[2]) < 5]
#
# print(RatingAbove5)

# {2022:,4,2021:6,2020:2}
movie = [mov for mov in movies]

MovYcount = {}
for mov in movie:
    if mov[1] in MovYcount:
        MovYcount[mov[1]] += 1
    else:
        MovYcount[mov[1]] = 1
print(MovYcount)
print(MovYcount.items())

MovieMax = max(MovYcount.items(), key=lambda iteam:iteam[1])
print(MovieMax)
