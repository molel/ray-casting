from settings import TILE_SIZE

_ = False
world_map = [[1, 1, 1, 1, 1, 1],
             [1, _, _, _, _, 1],
             [1, _, _, _, _, 1],
             [1, _, _, _, 1, 1],
             [1, _, _, 1, 1, 1],
             [1, 1, 1, 1, 1, 1]]

walls = set((j * TILE_SIZE, i * TILE_SIZE)
            for i in range(len(world_map))
            for j in range(len(world_map[i]))
            if world_map[i][j] == 1)
