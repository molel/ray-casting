world_map = ["WWWWWWWW",
             "W......W",
             "W......W",
             "W......W",
             "W......W",
             "W......W",
             "W......W",
             "WWWWWWWW"]

walls = tuple((i, j) for i in range(len(world_map)) for j in range(len(world_map[i])) if world_map[i][j] == "W")
