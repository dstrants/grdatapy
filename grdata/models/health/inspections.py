from typing import Optional
from pydantic import BaseModel


class Inspection(BaseModel):
    """
    EFET inspection model.
    Reprents the year summary of efet inspection within the country.

    year -> The year of the summary.
    inspections -> Total inspections for the whole year.
    violations -> Total violations for the whole year.
    violating_organizations -> Number of organization found violating the regulations.
    penalties -> Total penalties issued the whole year.
    """
    year: int
    inspections: Optional[int] = 0
    violations: Optional[int] = 0
    violating_organizations: int
    penalties: int

    @property
    def violation_ratio(self) -> Optional[float]:
        """Calculates the ration of the violations vs the inspections."""
        if not self.inspections:
            return None

        return round(self.violations / self.inspections, 2)


class InspectionList(BaseModel):
    """Parent model for inpsections."""
    items: list[Inspection]
