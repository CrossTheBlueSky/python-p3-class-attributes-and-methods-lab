class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    
    def __init__(self, name, artist, genre):
        Song.count+= 1
        self.name = name
        self.artist = artist
        self.genre = genre

        if artist not in Song.artists:
            Song.artists.append(artist)
            Song.artist_count[f"{artist}"] = 1
        else:
            Song.artist_count[artist] +=1

        
        if genre not in Song.genres:
            Song.genres.append(genre)
            Song.genre_count[f"{genre}"] =1
        else:
            Song.genre_count[genre] +=1    




    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    
    name = property(get_name, set_name)

    def get_artist(self):
        return self._artist

    def set_artist(self, artist):
        self._artist = artist

    artist = property(get_artist, set_artist)

    def get_genre(self):
        return self._genre
    
    def set_genre(self, genre):
        self._genre = genre

    genre = property(get_genre, set_genre)


