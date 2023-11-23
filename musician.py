class Musician:
    def __init__(self, name, genre, members=None):
        self.name = name
        self.genre = genre
        self.members = members if members is not None else []
        self.albums = []

    def add_member(self, member_name, role):
        member = {"name": member_name, "role": role}
        self.members.append(member)

    def add_album(self, album_title, release_year, songs=None):
        album = {"title": album_title, "release_year": release_year, "songs": songs if songs is not None else []}
        self.albums.append(album)

    def add_song_to_album(self, album_title, song_title, duration):
        for album in self.albums:
            if album["title"] == album_title:
                song = {"title": song_title, "duration": duration}
                album["songs"].append(song)
                return

    def get_members(self):
        return self.members

    def get_albums(self):
        return self.albums

    def get_discography(self):
        discography = {}
        for album in self.albums:
            discography[album["title"]] = {"release_year": album["release_year"], "songs": album["songs"]}
        return discography
