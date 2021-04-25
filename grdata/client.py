import os
from typing import Optional
import requests

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

        

        