from typing import Optional

from pydantic import BaseModel


class QuarterBasedModel(BaseModel):
    """
    Abstraction Model to replicate the below pattern.

    year -> The year of the statistics.
    quaertert -> The quarter of the statistics.
    active -> Number of active entries for the givern quarter.
    entrants -> New entries for the given quarter.
    exits -> Retired entries for the given quarter.
    """
    year: int
    quarter: str
    active: int
    entrants: Optional[int]
    exits: Optional[int]