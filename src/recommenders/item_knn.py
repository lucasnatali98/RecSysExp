from src.recommenders.recommender import Recommender
from lenskit.algorithms import item_knn
from src.utils import process_parameters


class ItemKNN(Recommender):
    def __init__(self, parameters: dict) -> None:

        default_keys = {
            'maxNumberNeighbors',
            'minNumberNeighbors',
            'saveNeighbors',
            'feedback'
        }

        parameters = process_parameters(parameters, default_keys)
        self.max_number_neighbors = parameters['maxNumberNeighbors']
        self.min_number_neighbors = parameters['minNumberNeighbors']
        self.save_nbrs = parameters['saveNeighbors']
        self.feedback = parameters['feedback']
        self.aggregate = parameters['aggregate']
        self.use_ratings = parameters['use_ratings']

        self.ItemKNN = item_knn.ItemItem(
            nnbrs=self.max_number_neighbors,
            min_nbrs=self.min_number_neighbors,
            save_nbrs=self.save_nbrs,
            feedback=self.feedback,
            aggregate=self.aggregate,
            use_ratings=self.use_ratings
        )


    def predict_for_users(self, users, items, ratings):
        """

        @param users:
        @param items:
        @param ratings:
        @return:
        """

        return self.ItemKNN.predict_for_user(users, items, ratings)

    def predict(self, pairs, ratings):
        """

        @param pairs:
        @param ratings:
        @return:
        """
        return self.ItemKNN.predict(pairs, ratings)

    def recommend(self, user, n, candidates, ratings):
        """

        @param user:
        @param n:;
        @param candidates:
        @param ratings:
        @return:
        """
        pass

    def get_params(self, deep=True):
        """

        @param deep:
        @return:
        """
        pass

    def fit(self, rating, **kwargs):
        """

        @param rating:
        @param kwargs:
        @return:
        """
        self.ItemKNN.fit(rating)
