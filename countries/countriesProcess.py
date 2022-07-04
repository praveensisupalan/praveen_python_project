import json

with open("countries.json", encoding="utf-8")as countries:
    CountriesList=json.load(countries)

# print total number of country details

print("total number of country details = ",len(CountriesList))

# print languages of ukrane

countryLan=[country["languages"] for country in CountriesList if country["name"]=="Afghanistan"]

print([i["name"] for i in countryLan[0]])

# print currency of china
countryCurr=[country["currencies"] for country in CountriesList if country["name"]=="China"]
print("currency of china= ",countryCurr[0][0]["name"])

# print population of india
countryPopul=[country["population"] for country in CountriesList if country["name"]=="India"]
print(countryPopul)

# print nigehbouring countries of australia
countryNig=[country["borders"] for country in CountriesList if country["name"]=="Afghanistan"]
print(countryNig)