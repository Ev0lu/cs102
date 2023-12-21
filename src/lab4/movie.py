class Cinema:

    """
    Класс, который реализует подбор фильма
    """

    def __init__(self, films_file, history_file, user_views):
        self.films_file = films_file
        self.history_file = history_file
        self.films = self.load_films()
        self.history = self.load_history()
        self.user_views = list(map(int, user_views.split(',')))

    def load_films(self):
        films = {}
        with open(self.films_file, 'r', encoding="utf-8") as file:
            for line in file:
                movie_id, movie_name = line.strip().split(',')
                films[int(movie_id)] = movie_name
        return films

    def load_history(self):
        history = []
        with open(self.history_file, 'r', encoding="utf-8") as file:
            for line in file:
                viewed_films = list(map(int, line.strip().split(',')))
                history.append(viewed_films)
        return history

    def filter_users(self):
        filtered_users = []
        for user in self.history:
            if set(self.user_views).issubset(set(user)):
                filtered_users.append(user)
        return filtered_users

    def exclude_watched_films(self, filtered_users):
        unwatched_films = []
        for user in filtered_users:
            unwatched_films.extend([movie for movie in user if movie not in self.user_views])
        return unwatched_films

    def recommend_movie(self):
        filtered_users = self.filter_users()
        unwatched_films = self.exclude_watched_films(filtered_users)

        movie_views_count = {}
        for movie in unwatched_films:
            movie_views_count[movie] = movie_views_count.get(movie, 0) + 1

        recommended_movie_id = max(movie_views_count, key=movie_views_count.get)
        recommended_movie_name = self.films[recommended_movie_id]

        print("Рекомендуемый фильм:", recommended_movie_name)


if __name__ == "__main__":
    films_file = 'films.txt'
    history_file = 'history.txt'
    user_views = '1, 2'
    recommendation_service = Cinema(films_file, history_file, user_views)
    recommendation_service.recommend_movie()
