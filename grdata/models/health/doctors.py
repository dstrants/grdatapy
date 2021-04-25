from pydantic import BaseModel

from grdata.models.health.generic import QuarterBasedModel as Qba


class Doctors(Qba):
    """
    Doctors operating in Greece within a quarter.

    year -> The year of the statistics.
    quaertert -> The quarter of the statistics.
    active -> Number of active doctors for the givern quarter.
    entrants -> New doctors for the given quarter.
    exits -> Retired doctors for the giver quarter.
    """


class DoctorsList(BaseModel):
    """Parent model for doctors model."""
    items: list[Doctors]
