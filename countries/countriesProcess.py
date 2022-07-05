import json

with open("countries.json", encoding="utf-8") as countries:
    CountriesList = json.load(countries)


def GetCountryData(CountryName):
    return [country for country in CountriesList if country["name"].lower().startswith(CountryName)]


# print total number of country details

print("total number of country details = ", len(CountriesList))

# print languages of Ukraine

countryLan = GetCountryData("ukraine")
lan = countryLan[0].get("languages")
print(lan[0].get("name"))

# print currency of Palestine
countryCurr = GetCountryData("palestine")
print([contry["name"] for contry in countryCurr["currencies"])
# print("currency of Palestine = ", [curr["name"] for curr in countryCurr[0]])

# print population of india
countryPopul = [country["population"] for country in CountriesList if country["name"] == "India"]
print("population of india = ", countryPopul[0])

# print nigehbouring countries of australia
countryNig = [country["borders"] for country in CountriesList if country["name"] == "Afghanistan"]
print("nigehbouring countries of australia = ", countryNig[0])

# print nigehbouring countries name of india

indiaBorder = GetCountryData("india")
borders = indiaBorder[0].get("borders")
sharingBorders = [country.get("name") for country in CountriesList if country["alpha3Code"] in borders]
print(sharingBorders)

# max populated country
maxPopulation = max(CountriesList, key=lambda country: country.get("population"))
print(maxPopulation["name"])

# min populated country

mixPopulation = min(CountriesList, key=lambda country: country.get("population"))
print(mixPopulation["name"])
