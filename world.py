from settings import TILE_SIZE

world_map = ["WWWWWWWW",
             "W......W",
             "W.W..W.W",
             "W.W..W.W",
             "W.W..W.W",
             "W.W..W.W",
             "W......W",
             "WWWWWWWW"]

walls = set((j * TILE_SIZE, i * TILE_SIZE)
            for i in range(len(world_map))
            for j in range(len(world_map[i]))
            if world_map[i][j] == "W")
