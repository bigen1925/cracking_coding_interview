from time import sleep
from typing import Dict


class Song:
    def __init__(self, name: str):
        self.name = name

    def play(self):
        print(self.name + " is playing ", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="\n\n")


class Jukebox:
    def __init__(self):
        self.songs: Dict[str, Song] = {}

    def add_song(self, key: str, song: Song) -> "Jukebox":
        self.songs[key] = song
        return self

    def add_songs(self, songs: Dict[str, Song]) -> "Jukebox":
        for key, song in songs.items():
            self.add_song(key, song)
        return self

    def run(self):
        while True:
            money = int(input("Please Insert Coin: "))
            if money < 100:
                print("You are poor.")
                continue

            print("Songs list is bellow.")
            for key, song in self.songs.items():
                print(key + ": " + song.name)

            key = input("\nPlease select a song key: ")
            while key not in self.songs:
                key = input("The key does not exist. Please reselect a song key: ")

            self.songs[key].play()

            print("")


if __name__ == "__main__":
    jukebox = Jukebox()
    jukebox.add_songs(
        {
            "1A": Song("Rolling Girl"),
            "2B": Song("Melt Down"),
            "3C": Song("World's End Dancehall"),
            "4D": Song("Panda Hero"),
        }
    )
    jukebox.run()
