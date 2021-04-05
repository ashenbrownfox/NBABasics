starting_lineup = [
    ["Guard", 9, "Miami Unviseristy", "Ron Harper"],
    ["Forward", 7, "Croatia", "Tony Kukoc"],
    ["Forward", 91, "Southeastern OKC", "Dennis Rodman"],
    ["Forward", 33, "Central Arkansas", "Scottie Pippen"],
    ["Guard", 23, "North Carolina", "Michael Jordan"],
]

for player in starting_lineup:
    position = player[0]
    jersey = player[1]
    college = player[2]
    name = player[3]
    player_string = f"At {position} number {jersey} from {college}, {name}!"
    print(player_string)
