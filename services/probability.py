import random


class ProbabilityService:
    @staticmethod
    def percentage_roll(probability: int) -> bool:
        return random.randint(0, 99) < probability
