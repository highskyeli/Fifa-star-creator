players = []


def createAcard(name, country, league):

    card = {

    }
    
    card["name"] = name 
    card["country"] =  country
    card["league"]  =  league

    if card["league"] not in ["Ligue1", "Premiere League", "La Liga", "MLS", "Serie A"]:
        league = input("Typed in a wrong league. What league would your player be in? ")
    players.append(card)
    
    


for i in range(11):

    name = input("What is your player's name? ")
    country = input("What is your player's country? ")
    league = input("what is your player's league? ")
    createAcard(name, country,league)
    print(players) 
    if name == "quit":
        break

