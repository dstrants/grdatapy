import datetime
import pendulum
from pydantic import BaseModel


class Vaccination(BaseModel):
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
        return pendulum.parser.parse(self.referencedate, tz='Europe/Athens')



class VaccinationList(BaseModel):
    items: list[BaseModel]

    @property
    def item_count(self) -> int:
        return len(self.items)

    def group_by_date(self) -> dict:
        unique_dates = {d.date for d in self.items}
        unique_dates = sorted(unique_dates, key=lambda k: k)
        results = {}
        for date in unique_dates:
            results[str(date)] = list(filter(lambda x: x.date == date, self.items))
        return results

