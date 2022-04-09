from pathlib import Path

import pandas as pd
import requests

COUNTRY_CODES = pd.read_csv(Path(__file__).parent / "country_codes.csv").set_index(
    "name"
)

COUNTRIES_EU = [
    "Austria",
    "Belgium",
    "Bulgaria",
    "Croatia",
    "Cyprus",
    "Czechia",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Ireland",
    "Italy",
    "Latvia",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Netherlands",
    "Poland",
    "Portugal",
    "Romania",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
]

COUNTRIES_V4 = ["Hungary", "Poland", "Czechia", "Slovakia"]

INDICATORS = {"GDP per capita, PPP (current international $)": "NY.GDP.PCAP.PP.CD"}


def get_country_indicator(country, indicator):
    if indicator in INDICATORS:
        indicator = INDICATORS[indicator]

    return requests.get(
        f"http://api.worldbank.org/v2/country/{COUNTRY_CODES.loc[country]['alpha-2']}/indicator/{indicator}?format=json"
    ).json()[1]
