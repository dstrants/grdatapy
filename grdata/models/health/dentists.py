from pydantic import BaseModel

from grdata.models.health.generic import QuarterBasedModel as Qba


class Dentists(Qba):
    """
    Dentists operating in Greece within a quarter.

    year -> The year of the statistics.
    quaertert -> The quarter of the statistics.
    active -> Number of active dentists for the givern quarter.
    entrants -> New dentists for the given quarter.
    exits -> Retired dentists for the giver quarter.
    """


class DentistsList(BaseModel):
    """Parent model for doctors model."""
    items: list[Dentists]
