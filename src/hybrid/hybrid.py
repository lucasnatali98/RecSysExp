
from src.recommenders.recommender import Recommender


class Hybrid(Recommender):

    def __init__(self, parameters: dict) -> None:
        self.constituent_algorithm = []

    def process_parameters(self, parameters: dict) -> dict:
        pass

    def add_algorithm(self, algorithm) -> None:
        """
        
        """
        pass
    def remove_algorithm(self, algorithm) -> None:
        """
        
        """
        pass