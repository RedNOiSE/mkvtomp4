import os
import subprocess
import urllib
import tmdbsimple as tmdb
from imdbpie import Imdb
#from mutagen.mp4 import MP4, MP4Cover

tmdb.API_KEY="3720151b81d502aa54a256233f6f5af8"

def file_info(file):
    """
    Retrieving movie information from www.themoviedb.org\n
    """
    search_index = 0
    fname = file[:-4]
    print("\nFetching information for '" + fname + "'")
    search = tmdb.Search()
    response = search.movie(query=fname)
    # getting a Movies object from tmdb
    try:
        tmdb_movie = tmdb.Movies(search.results[search_index]['id'])
    except IndexError:
        while len(search.results) == 0:
            title = input("\nUnable to find the movie, Enter movie title >> ")
            search_index = int(input('Search result index >> '))
            response = search.movie(query=title)
            try:
                tmdb_movie = (tmdb.movies(search.results[search_index]['id']))
            except IndexError:
                continue
    # we get info about the movie
    response = tmdb_movie.info()
    # making imdb object
    imdb = Imdb()
    imdb_movie = imdb.get_title_by_id(tmdb_movie.imdb_id)
    new_filename = (imdb_movie.title + '(' + str(imdb_movie.year) + ').mp4')
    new_filename = (new_filename
                    .replace(':', '-')
                    .replace('/', ' ')
                    .replace('?', ''))
    print("\n" + new_filename)
    print("\nFetching the movie poster...")
    poster_filename = fname[:-4] + '.jpg'
    path = search.results[search_index]['poster_path']
    poster_path = r'https://image.tmdb.org/t/p/w640' + poster
    url_obj = urllib.request.urlopen(poster_path)
    with open(poster_filename,"wb") as poster_file:
        poster_file.write(url_obj.read())
        poster_file.close()
    imdb_rating_and_plot = str('IMDB rating ['
                               + str(float(imdb_movie.rating))
                               + '/10] - '
                               + imdb_movie.plot_outline)
    genre = ';'.join(imdb_movie.genres)
    director = imdb_movie.directors_summary[0].name
    print("\nIMDB rating: " + imdb_rating_and_plot)
    print("\nGenre(s): " + genre)
    print("\nDirector: " + director)

if __name__ == '__main__':
    file_info("e:\Video\Робот по имени Чаппи (2015).mp4")
