from collections.abc import Iterable, Iterator
from typing import Any


class Song:
    """
    Represents a song with a title and an artist.
    """

    def __init__(self, title: str, artist: str) -> None:
        self.title = title
        self.artist = artist

    def __str__(self) -> str:
        return f"{self.title} by {self.artist}"


class AlphabeticalOrderIterator(Iterator):
    """
    Iterator that allows traversing a collection in direct or reverse order.
    """

    _position: int = None
    _reverse: bool = False

    def __init__(
        self,
        collection: "WordsCollection",
        reverse: bool = False,
    ) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class WordsCollection(Iterable):
    """
    Collection that implements an iterator to traverse elements.
    """

    def __init__(self, collection: list[Any] | None = None) -> None:
        self._collection = collection or []

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item: Any) -> None:
        self._collection.append(item)


class Playlist(WordsCollection):
    """
    The collection of songs acts as a playlist.
    Inherits from WordsCollection and uses its iteration logic.
    """

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return f"Playlist: {self.name}"


if __name__ == "__main__":
    # Create a playlist and add songs.
    playlist = Playlist("My Favorite Songs")
    playlist.add_item(Song("Bohemian Rhapsody", "Queen"))
    playlist.add_item(Song("Stairway to Heaven", "Led Zeppelin"))
    playlist.add_item(Song("Hotel California", "Eagles"))

    # Playback in order.
    print(f"Straight traversal of {playlist}:")
    for song in playlist:
        print(song)

    print("")

    # Playback in reverse order.
    print(f"Reverse traversal of {playlist}:")
    for song in playlist.get_reverse_iterator():
        print(song)
