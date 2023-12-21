import unittest
from movie import Cinema


class TestCinema(unittest.TestCase):

    def setUp(self):
        self.films_file = "films.txt"
        self.history_file = "history.txt"
        self.user_views = "1,2,3"
        self.cinema = Cinema(
            self.films_file, self.history_file, self.user_views)

    def test_load_films(self):
        expected_films = {1: 'Мстители: Финал', 2: 'Хатико',
                          3: 'Дюна', 4: 'Унесенные призраками'}
        self.assertEqual(self.cinema.load_films(), expected_films)

    def test_load_history(self):
        expected_history = [[2, 1, 3], [1, 4, 3], [2, 2, 2, 2, 2, 3]]
        self.assertEqual(self.cinema.load_history(), expected_history)

    def test_filter_users(self):
        expected_filtered_users = [[2, 1, 3]]
        self.assertEqual(self.cinema.filter_users(), expected_filtered_users)

    def test_exclude_watched_films(self):
        filtered_users = self.cinema.filter_users()
        expected_unwatched_films = []
        self.assertEqual(self.cinema.exclude_watched_films(
            filtered_users), expected_unwatched_films)


if __name__ == 'main':
    unittest.main()