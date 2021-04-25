# Greek data API python client
This repo is a simple client for the greek open data platform written in python. This work is inspired by the [similar endiavour](https://github.com/ppapapetrou76/go-data-gov-gr-sdk) writen in Go from [@ppapapetrou76](https://github.com/ppapapetrou76)!

**Note**: _I plan to add a cli, hopefully I will find the time to do so after adding all the available endpoints_
**Note2**: _Some of the endpoints are greatly outdated. Always refer to the [official site](https://data.gov.gr/) for the available time ranges._


## Endpoints available

### Health
Endpoint related to national health systems

Name | Description | client method | Status
-----|-------------|---------------|--------
vaccinations | CoVid 19 vaccination stats per region per day | `.vaccinations` | ✅
efet_inpection | Number of efet inpections per year | `.efet_inspections` | ✅
pharmacists | Number of existing, new, and retired pharmacists per quarter | `.pharmacists` | ✅
pharmacies | Number of existing, new, and closed pharmacies per quarter | `.pharmacies` | ✅
doctors | Number of existing, new, and retired doctors per quarter | `.doctors` | ✅
dentists | Number of existing, new, and retired dentists per quarter | `.dentists` | ✅


### Usage example
This section is a very minimal introduction into the client. I will try to generate the docs soon to offer a more complete documentation.

To iniate the client you need an API key that you can retrieve from [here](https://data.gov.gr/token/). After filling in the form, you will receive an email with personal api token. You can pass the token either as an argument to the `Client` class or as an enviroment varialbe `GRDATA_API_KEY`. If you do not pass the key as an argument the environment variable will be used as a fallback. If none of this is filled in the client will raise a `ValueError`.

```python
# Using the token as argument
client = Client("my_api_key_value")

# doctors
client.doctors()

# Vaccinations                     # from date    # to date
vaccinations = client.vaccinations("2021-04-01", "2021-04-20")

# Basic aggregation per date (more to be added soon 🤞🏽)
vaccinations.group_by_date()
```