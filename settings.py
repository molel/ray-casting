from math import pi, tan

# Window settings
RES = WIDTH, HEIGHT = 800, 800
HALF_OF_WIDTH, HALF_OF_HEIGHT = WIDTH // 2, HEIGHT // 2
FPS = 60

# Ray casting settings
TILE_SIZE = 80
FOV = pi / 3
POV = 0
NUMBER_OF_RAYS = 400
DOV = NUMBER_OF_RAYS / (2 * tan(FOV / 2))
DELTA_RAY = FOV / NUMBER_OF_RAYS
RAY_WIDTH = WIDTH // NUMBER_OF_RAYS
PROJECTION_SCALE = DOV * TILE_SIZE * 2

# Colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 100, 200, 100
LIGHT_BLUE = 124, 165, 235
GRAY = 44, 80, 80

# Player settings
POS = HALF_OF_WIDTH // 2, HALF_OF_HEIGHT // 2
STEP = 5

# Texture settings
TEXTURE_WIDTH = 240
TEXTURE_HEIGHT = 240
TEXTURE_SCALE = TEXTURE_WIDTH // TILE_SIZE

# Minimap settings
MINIMAP_SCALE = 1 / 4
MINIMAP_WIDTH = WIDTH * MINIMAP_SCALE
MINIMAP_HEIGHT = HEIGHT * MINIMAP_SCALE
MINIMAP_TILE_SIZE = TILE_SIZE * MINIMAP_SCALE

# Other settings
DOUBLE_PI = pi * 2
