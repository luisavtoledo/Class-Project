import unittest
from musician import Musician

class TestMusician(unittest.TestCase):
    def setUp(self):
        self.my_band = Musician(name="Lady Gaga", genre="Pop")

    def test_add_member(self):
        self.my_band.add_member("Johnny", "Bass")
        self.assertEqual(len(self.my_band.members), 1, "Add member failed")

    def test_add_album(self):
        self.my_band.add_album("Born This Way", 2011, songs=[{"title": "The Edge of Glory", "duration": 321}, {"title": "Bad Kids", "duration": 231}])
        self.assertEqual(len(self.my_band.albums), 1, "Add album failed")

    def test_add_song_to_album(self):
        self.my_band.add_album("The Fame", 2008, songs=[{"title": "Poker Face", "duration": 238}])
        self.my_band.add_song_to_album("The Fame", "Just Dance", 300)
        album = next(album for album in self.my_band.albums if album["title"] == "The Fame")
        self.assertEqual(len(album["songs"]), 2, "Add song to album failed")

    def test_get_members(self):
        self.my_band.add_member("Stefani", "Piano")
        members = self.my_band.get_members()
        self.assertEqual(len(members), 1, "Get members failed")

    def test_get_albums(self):
        self.my_band.add_album("ARTPOP", 2013, songs=[{"title": "Gypsy", "duration": 360}])
        albums = self.my_band.get_albums()
        self.assertEqual(len(albums), 1, "Get albums failed")

    def test_get_discography(self):
        self.my_band.add_album("The Fame Monster", 2010, songs=[{"title": "Bad Romance", "duration": 330}])
        discography = self.my_band.get_discography()
        self.assertEqual(len(discography), 1, "Get discography failed")