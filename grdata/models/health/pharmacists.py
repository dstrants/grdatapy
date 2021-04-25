from pydantic import BaseModel

from grdata.models.health.generic import QuarterBasedModel as Qbm


class Pharmacists(Qbm):
    """
    Pharmasicts operating in Greece within a quarter.

    year -> The year of the statistics.
    quaertert -> The quarter of the statistics.
    active -> Number of active pharmacists for the givern quarter.
    entrants -> New pharmacists for the given quarter.
    exits -> Retired pharmacists for the giver quarter.
    """   

class Pharmacies(Qbm):
    """
    Pharmasies operating in Greece within a quarter.

    year -> The year of the statistics.
    quaertert -> The quarter of the statistics.
    active -> Number of active pharmacies for the givern quarter.
    entrants -> New pharmacies for the given quarter.
    exits -> Closed pharmacies for the giver quarter.
    """  


class PharmasictsList(BaseModel):
    """Parent model for the Pharmacists statistics model."""
    items: list[Pharmacists]

class PharmasiesList(BaseModel):
    """Parent model for the Pharmacies statistics model."""
    items: list[Pharmacies]
