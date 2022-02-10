from random import choice
import pygame
from enemy import Enemy
from ui import UI
from weapon import Weapon
from player import Player
from settings import *
from tile import Tile
from debug import debug
from support import *


class Level:
    def __init__(self):
        # get display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

        # interfaccia
        self.ui = UI()

    def create_map(self):
        # dizionario del layout e delle grafiche
        layouts = {
            "boundary": import_csv_layout("map/map_FloorBlocks.csv"),
            "grass": import_csv_layout("map/map_Grass.csv"),
            "object": import_csv_layout("map/map_Objects.csv"),
            "entities": import_csv_layout("map/map_Entities.csv"),
        }
        graphics = {
            "grass": import_folder("graphics/grass"),
            "objects": import_folder("graphics/objects"),
        }
        # print(graphics)

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != "-1":
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                        # creazione del bordo della mappa
                        if style == "boundary":
                            Tile((x, y), [self.obstacle_sprites], "invisible")

                        # creazione degli oggetti erbosi sulla mappa
                        if style == "grass":
                            random_grass_image = choice(graphics["grass"])
                            Tile(
                                (x, y),
                                [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites],
                                "grass",
                                random_grass_image,
                            )

                        # creazione degli oggetti di scena
                        if style == "object":
                            surf = graphics["objects"][int(col)]
                            Tile(
                                (x, y),
                                [self.visible_sprites, self.obstacle_sprites],
                                "object",
                                surf,
                            )

                        if style == "entities":
                            # 394 numero nel file dei tile del giocatore
                            if col == "394":
                                # posizione del giocatore a circa il centro della mappa
                                self.player = Player(
                                    (x, y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.create_magic,
                                    self.destroy_attack,
                                )
                            else:
                                if col == "390":
                                    monster_name = "bamboo"
                                elif col == "391":
                                    monster_name = "spirit"
                                elif col == "392":
                                    monster_name = "raccoon"
                                else:
                                    monster_name = "squid"
                                Enemy(
                                    monster_name,
                                    (x, y),
                                    [self.visible_sprites, self.attackable_sprites],
                                    self.obstacle_sprites, self.damage_player
                                )

    def create_magic(self, style, strength, cost):
        print(style)
        print(strength)
        print(cost)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
        self.ui.display(self.player)
        # debug(self.player.status)

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites=pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == "grass":
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player, attack_sprite.sprite_type)

    def damage_player(self, amount, attack_type):
        if self.player.vulnerable:
            self.player.health-=amount
            self.player.vulnerable=False
            self.player.hurt_time=pygame.time.get_ticks()

            # particelle


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creazione del piano
        self.floor_surf = pygame.image.load("graphics/tilemap/ground.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # disegno del piano
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        # nel momento in cui creo la mappa, alcuni blocchi vengono creati dopo il giocatore. Ordino i blocchi in modo che il giocatore, quando si trova sotto un blocco, sia più in avanti
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self, player):
        enemy_sprites = [
            sprite
            for sprite in self.sprites()
            if hasattr(sprite, "sprite_type") and sprite.sprite_type == "enemy"
        ]
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
