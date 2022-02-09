import pygame

# classe con i metodi in comune tra il giocatore e i nemici
class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

    def move(self, speed):
        if (
            self.direction.magnitude() != 0
        ):  # controllo la lunghezza del vettore direzione
            self.direction = (
                self.direction.normalize()
            )  # normalizzo la dimensione del vettore

        self.hitbox.x += self.direction.x * speed
        self.collision("horizontal")
        self.hitbox.y += self.direction.y * speed
        self.collision("vertical")

        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # movimento verso destra
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # movimento verso sinistra
                        self.hitbox.left = sprite.hitbox.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # movimento verso il basso
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # movimento verso l'alto
                        self.hitbox.top = sprite.hitbox.bottom
