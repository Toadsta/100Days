travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, times_visited, cities_visited):
    travel_log.append( 
    {
      "country": country,
      "visits": times_visited,
      "cities": cities_visited,
    },
    )
     
countryInput = input("Which country did you go to?\n")
visitedInput = int(input(f"How many times have you visited {countryInput}?\n"))
citiesInput = []
shouldContinue = "yes"
while shouldContinue == "yes":
    citiesInput.append(input(f"What city have you visited in {countryInput}?\n"))
    shouldContinue = input(f"Have you visited any other cities in {countryInput}?\n")


add_new_country(countryInput, visitedInput, citiesInput )
print(travel_log)



