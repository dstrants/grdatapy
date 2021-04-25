import datetime
import pendulum
from pydantic import BaseModel


class Vaccination(BaseModel):
    """
    Vaccination data model
    
    Vaccination stats for a given region and date.

    area -> Name of the given area.
    areid -> Numeric id of the given area.
    dailydose1 -> Number of first doses administrated for the given date.
    dailydose2 -> Number of second doses administrated for the given date.
    daydiff -> Difference in administrated doses (in total) with the previous date.
    referencedate -> The given date.
    totaldistinctpersons -> The total unique people that had been administrated at lease
    a single dose since day one of the vaccinacion programme.
    totaldose1 -> Total number of first dose administrations.
    totaldose2 -> Total number of second dose administrations.
    totalvaccinnations: Total number of doses administrated.
    """
    area: str
    areaid: int
    dailydose1: int
    dailydose2: int
    daydiff: int
    referencedate: str
    totaldistinctpersons: int
    totaldose1: int
    totaldose2: int
    totalvaccinations: int

    @property
    def date(self) -> datetime.datetime:
        """Returns the given date in datetime object."""
        return pendulum.parser.parse(self.referencedate, tz='Europe/Athens')



class VaccinationList(BaseModel):
    """Parent model for the vaccinations stats."""
    items: list[BaseModel]

    @property
    def item_count(self) -> int:
        """Number of entities (vaccination stats) nested in model."""
        return len(self.items)

    def group_by_date(self) -> dict:
        """Groups nested entities by date."""
        unique_dates = {d.date for d in self.items}
        unique_dates = sorted(unique_dates, key=lambda k: k)
        results = {}
        for date in unique_dates:
            results[str(date)] = list(filter(lambda x: x.date == date, self.items))
        return results
