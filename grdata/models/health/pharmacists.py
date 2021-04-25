from typing import Optional
from pydantic import BaseModel


class Pharmacists(BaseModel):
    """
    Pharmasicts operating in Greece within a quarter.

    year -> The year of the statistics.
    quaertert -> The quarter of the statistics.
    active -> Number of active pharmacists for the givern quarter.
    entrants -> New pharmacists for the given quarter.
    exits -> Retired pharmacists for the giver quarter.
    """
    year: int
    quarter: str
    active: int
    entrants: Optional[int]
    exits: Optional[int]    

class PharmasictsList(BaseModel):
    """Parent model for the Pharmacists statistics model."""
    items: list[Pharmacists]