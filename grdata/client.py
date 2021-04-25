import os
from typing import Optional
import requests

from grdata.models.health.dentists import Dentists, DentistsList
from grdata.models.health.doctors import Doctors, DoctorsList
from grdata.models.health.inspections import Inspection, InspectionList
from grdata.models.health.pharmacists import Pharmacists, Pharmacies, PharmasictsList, PharmasiesList
from grdata.models.health.vaccination import Vaccination, VaccinationList



class Client:
    def __init__(self, api_key: Optional[str] = None) -> None:
        if not (key := api_key):
            key = os.environ.get("GRDATA_API_KEY")

        if not key:
            raise ValueError("Api key cannot be empty")

        self.api_key: str = key
        self.base_url = 'https://data.gov.gr/api/v1/query/'

    def get(self, endpoint: str, params: dict = {}, headers: dict = {}) -> dict:
        """
        Abstract method that performs all connections with the API.
        """
        hed = {'Authorization': f'Token {self.api_key}'} | headers
        url = self.base_url + endpoint
        response = requests.get(url, params=params, headers=hed)

        response.raise_for_status()

        return response.json()

    def vaccinations(self, from_date: str, to_date: str) -> VaccinationList:
        """
        Daily vaccinations per region per day for the give date range.
        """
        params = {'date_from': from_date, 'date_to': to_date}
        data = self.get("mdg_emvolio", params=params)

        ls  = [Vaccination(**area) for area in data]
        return VaccinationList(items=ls)

    def efet_inspections(self) -> InspectionList:
        data = self.get("efet_inspections")

        ls  = [Inspection(**ins) for ins in data]
        return InspectionList(items=ls)
    
    def pharmacists(self) -> PharmasictsList:
        data = self.get("minhealth_pharmacists")
        
        ls = [Pharmacists(**pharm) for pharm in data]
        return PharmasictsList(items=ls)
    
    def pharmacies(self) -> PharmasiesList:
        data = self.get("minhealth_pharmacies")
        
        ls = [Pharmacies(**pharm) for pharm in data]
        return PharmasiesList(items=ls)

    def doctors(self) -> DoctorsList:
        data = self.get("minhealth_doctors")
        
        ls = [Doctors(**doc) for doc in data]
        return DoctorsList(items=ls)
    
    def dentists(self) -> DentistsList:
        data = self.get("minhealth_dentists")
        
        ls = [Dentists(**dent) for dent in data]
        return DentistsList(items=ls)
