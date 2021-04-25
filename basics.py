starting_lineup_bulls = [
    {"position": "Guard", "jersey": 9,
        "college": "Miami Unviseristy", "name": "Ron Harper"},
    {"position": "Forward", "jersey": 7, "college": "Croatia", "name": "Tony Kukoc"},
    {"position": "Forward", "jersey": 91,
        "college": "Southeastern OKC", "name": "Dennis Rodman"},
    {"position": "Forward", "jersey": 33,
        "college": "Central Arkansas", "name": "Scottie Pippen"},
    {"position": "Guard", "jersey": 23,
        "college":  "North Carolina", "name": "Michael Jordan"},
]
starting_lineup_warriors = [
    {"position": "Guard", "jersey": 9,
        "college": "Miami Unviseristy", "name": "Andre Igoudala"},
    {"position": "Forward", "jersey": 7,
        "college": "Michigan State", "name": "Draymond Green"},
    {"position": "Guard", "jersey": 11,
        "college": "Washington St", "name": "Klay Thompson"},
    {"position": "Forward", "jersey": 35,
        "college": "Texas", "name": "Kevin Durant"},
    {"position": "Guard", "jersey": 30,
        "college":  "Davidson", "name": "Stephen Curry"},
]

for player in starting_lineup_warriors:
    position = player["position"]
    jersey = player["jersey"]
    college = player["college"]
    name = player["name"]
    player_string = f"At {position} number {jersey} from {college}, {name}!"
    print(player_string)
