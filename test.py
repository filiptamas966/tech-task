import unittest
from bs4 import BeautifulSoup
from selenium import webdriver


class TestRadioPlayer(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.capitalfm.com/"
        # Path to installed ChromeDriver
        self.chrome_path = '/local/path/to/chromedriver'

    def test_recent_artist_justin_bieber(self):
        searched_artist = 'Justin Bieber'

        driver = webdriver.Chrome(executable_path=self.chrome_path)
        driver.get(self.url)
        updated_html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(updated_html, 'html.parser')

        now_playing_loader = soup.find('div', class_='now_playing_card_loader')
        now_playing_card = now_playing_loader.find('div', class_='now_playing_card')

        if now_playing_card:
            # Verify currently playing track
            now_playing_song = now_playing_card.find('article', class_='card_top_track')
            artist = now_playing_song.find('div', class_='artist')
            artist_name = artist.find('a', class_='first').text.strip()
            currently_playing = searched_artist in artist_name

            # Verify the other 3 recently played tracks
            recently_played_tracks = now_playing_card.find_all('article', class_='recently_played_track')
            recently_played = False
            for recently_played_track in recently_played_tracks:
                artist_name = recently_played_track.find('div', class_='artist').text.strip()
                if searched_artist in artist_name:
                    recently_played = True

            self.assertEqual(True, currently_playing or recently_played, f"Justin Bieber is not playing and has not played recently")

        else:
            self.fail('Could not find information about the currently playing song.')


if __name__ == "__main__":
    unittest.main()
