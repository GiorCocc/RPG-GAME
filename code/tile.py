import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(
        self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))
    ):
        super().__init__(groups)

        self.sprite_type = sprite_type
        y_offset=HITBOX_OFFSET[sprite_type]
        self.image = surface

        # creazione dei tile oggetto che sono più grandi dei tile classici
        if sprite_type == "object":
            self.rect = self.image.get_rect(
                topleft=(pos[0], pos[1] - TILESIZE)
            )  # modifica y in modo che coincida con quella di un tile classico (128 - 64)
        else:
            self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(
            0, y_offset
        )  # cambia la dimensione di rect lasciando intatto il centro
