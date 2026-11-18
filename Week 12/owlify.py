import time

class Song:
    def __init__(self, title, artist, album, genre, duration):
        self.title = title
        self.artist = artist
        self.album = album # Album object
        self.genre = genre
        self.duration = duration # in seconds

    def play(self):
        print(f"Playing {self.get_song_info()}.")
        time.sleep(self.duration)
        print(f"{self.get_song_info()} finished playing.")

    def get_song_info(self):
        return f"{self.title} by {self.artist}"

class Album:
    def __init__(self, title, artist, songs):
        self.title = title
        self.artist = artist
        self.songs = songs # List of Song objects

    def play(self):
        print(f"Playing album {self.get_album_info()}")
        for song in self.songs:
            song.play()
        print(f"{self.get_album_info()} finished playing.")

    def get_album_info(self):
        return f"{self.title} by {self.artist}"

class Playlist:
    def __init__(self, title, owner):
        self.title = title
        self.owner = owner
        self.songs = [] # List of Song objects

    def play(self):
        print(f"Playing Playlist {self.get_playlist_info()}")
        for song in self.songs:
            song.play()
        print(f"{self.get_playlist_info()} finished playing.")

    def add_song(self, song):
        self.songs.append(song)

    def get_playlist_info(self):
        return f"{self.title} by {self.owner}"

def main():
    album_1 = Album("24K Magic", "Bruno Mars", [])
    song_1 = Song("24K Magic", "Bruno Mars", album_1, "Pop", 3)
    song_2 = Song("That's What I Like", "Bruno Mars", album_1, "Pop", 3)
    song_3 = Song("Versace on the Floor", "Bruno Mars", album_1, "Pop", 3)
    song_4 = Song("Chunky", "Bruno Mars", album_1, "Pop", 3)
    song_5 = Song("Finesse", "Bruno Mars", album_1, "Pop", 3)

    album_1.songs = [song_1, song_2, song_3, song_4, song_5]

    album_2 = Album("The Black Album", "Prince", [])
    song_6 = Song("Le Grind", "Prince", album_2, "Funk", 2)
    song_7 = Song("Cindy C.", "Prince", album_2, "Funk", 2)
    song_8 = Song("Dead on It", "Prince", album_2, "Funk", 2)
    song_9 = Song("When 2 R in Love", "Prince", album_2, "Funk", 2)
    album_2.songs = [song_6, song_7, song_8, song_9]

    playlist_1 = Playlist("My Playlist #1", "Eun Sik")
    playlist_1.add_song(song_4)
    playlist_1.add_song(song_8)

    song_7.play()
    print()
    album_1.play()
    print()
    playlist_1.play()

if __name__ == "__main__":
    main()