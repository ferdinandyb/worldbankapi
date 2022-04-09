# Helper for the World Bank API


## Example usage

```
from worldbankapi import get_country_indicator as gci
data = gci("Hungary", "NY.GDP.PCAP.PP.CD")
```

## Country names

The World Bank API (v2) actually uses country codes, so the country_codes.csv is loaded as
a pandas.DataFrame into the constant `worldbankapi.COUNTRY_CODES` for accessing them, so use the country names you find there.

The csv is from [Luke Duncalfe](https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv)'s github.

There are two convenience list of country names: `COUNTRIES_EU` and
`COUNTRIES_V4`.

## Indicators

To find the codes of indicators go to the [World Bank
website](https://data.worldbank.org/indicator/?tab=all), open the one you want
and get the indicator code from the URL. If you know a better way, let me know
:)

There is also an INDICATORS convenience dictionary that maps the names of the
indicators to their codes, but currently it has a single manual entry. Passing
these names to the function also works:

```
gci("Hungary","GDP per capita, PPP (current international $)")
```

# TODO

Scrape the https://data.worldbank.org/indicator/?tab=all website for links with
the form https://data.worldbank.org/indicator/EG.ELC.ACCS.RU.ZS?view=chart to
fill out INDICATORS.
