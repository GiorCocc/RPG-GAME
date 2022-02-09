import pygame
from settings import *
from entity import Entity
from support import *


class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, obstacle_sprites):
        # general setup
        super().__init__(groups)
        self.sprite_type = "enemy"

        # grafiche
        self.import_graphics(monster_name)
        self.status = "idle"
        self.image = self.animations[self.status][self.frame_index]

        # movimento
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # valori
        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]
        self.health = monster_info["health"]
        self.exp = monster_info["exp"]
        self.speed = monster_info["speed"]
        self.attack_damage = monster_info["damage"]
        self.resistance = monster_info["resistance"]
        self.attack_radius = monster_info["attack_radius"]
        self.notice_radius = monster_info["notice_radius"]
        self.attack_type = monster_info["attack_type"]

        # interazioni
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400

    def import_graphics(self, name):
        # dizionario delle possibili animazioni
        self.animations = {"idle": [], "move": [], "attack": []}
        main_path = f"graphics/monsters/{name}/"

        # assegnazione del corretto import delle immagini
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)

        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = (
                pygame.math.Vector2()
            )  # impongo che la direzione del movimento sia (0,0)

        return (distance, direction)

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        # il nemico può attaccare solo quando il giocatore entra nella sua zona di attacco, mentre se è nella sua zona "visiva" allora il nemico si muove verso il giocatore; altrimenti, quando il giocatore è lontano, lui è in idle
        if distance <= self.attack_radius and self.can_attack == True:
            if self.status != "attack":
                self.frame_index = 0
            self.status = "attack"
        elif distance <= self.notice_radius:
            self.status = "move"
        else:
            self.status = "idle"

    def actions(self, player):
        if self.status == "attack":
            self.attack_time = pygame.time.get_ticks()  # time per gli attacchi
        elif self.status == "move":
            self.direction = self.get_player_distance_direction(player)[
                1
            ]  # movimento in direzione del giocatore
        else:
            self.direction = (
                pygame.math.Vector2()
            )  # in idle deve rimanere fermo, quindi direzione (0,0)

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed

        if self.frame_index >= len(animation):
            if self.status == "attack":
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def cooldown(self):
        # timer per gli attacchi
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

    def update(self):
        self.move(self.speed)
        self.animate()
        self.cooldown()

    def enemy_update(self, player):
        self.get_status(player)
        self.actions(player)