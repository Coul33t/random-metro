import math

import pygame

WHITE = (255, 255, 255)

def draw_stations(screen, metro, font):
    for i, station in enumerate(metro.stations_list):
        pygame.draw.circle(screen, 
                            WHITE,
                            (int(station.coordinates[0] * metro.tile_size[0] + metro.tile_size[0] / 2),
                            int(station.coordinates[1] * metro.tile_size[0] + metro.tile_size[1] / 2)),
                            15)

        textsurface = font.render(str(i), True, (0, 0, 0))
        screen.blit(textsurface, (int(station.coordinates[0] * metro.tile_size[0] + 15),
                                  int(station.coordinates[1] * metro.tile_size[0])))

def draw_path(screen, metro, station):
    for a, b in zip(station.paths_to_other_station[:-1], station.paths_to_other_station[1:]):
        pygame.draw.line(screen, WHITE, (a[0] * metro.tile_size[0] - metro.tile_size[0] / 2, 
                                         a[1] * metro.tile_size[1] - metro.tile_size[1] / 2), 
                                        (b[0] * metro.tile_size[0] - metro.tile_size[0] / 2,
                                         b[1] * metro.tile_size[1] - metro.tile_size[1] / 2))

def draw_map(screen, metro, font):
    draw_stations(screen, metro, font)

    for station in metro.stations_list:
        draw_path(screen, metro, station)

def draw_test(screen):
    pygame.draw.line(screen, WHITE, (250, 250), (500, 250))
    pygame.draw.line(screen, WHITE, (500, 250), (600, 350))

def display(metro):
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Random Metro")
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    metro.generate_random_metro()
                    draw_map(screen, metro, font)
                    pygame.display.flip()