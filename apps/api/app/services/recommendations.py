from dataclasses import dataclass
from math import exp

@dataclass
class Candidate:
    product_id: str
    relevance: float
    proximity: float
    popularity: float
    freshness: float
    quality: float
    delivery_speed: float

def score(c: Candidate) -> float:
    # MVP ranking. Tune weights using real interaction data.
    return (
        .30*c.relevance +
        .20*c.proximity +
        .15*c.popularity +
        .15*c.freshness +
        .10*c.quality +
        .10*c.delivery_speed
    )

def surprise_score(c: Candidate, randomness: float = .15) -> float:
    # Controlled exploration: enough randomness to avoid always returning the winner.
    return score(c) + randomness * ((hash(c.product_id) % 1000) / 1000)
