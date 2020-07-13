import random as rn

import numpy as np

class Tile:
    def __init__(self, directions=None, tile_type=None):
        self.directions = directions
        if not directions:
            self.directions = np.zeros((3, 3))

        self.tile_type = tile_type

        self.coordinates = [-1, -1]

        self.is_linked = False
        self.paths_to_other_station = []

class Metro:
    def __init__(self):
        # Unit: tiles
        self.grid_size = (15, 15)
        self.grid = []
        # Unit: pixels
        self.tile_size = (50, 50)

        self.stations_list = []

    def initialise(self):
        self.grid = [[Tile() for x in range(self.grid_size[0])] for y in range(self.grid_size[1])]
        self.stations_list = []

    def generate_stations(self):
        number_of_stations = rn.randint(5, 20)

        for i in range(number_of_stations):
            row = rn.randint(0, self.grid_size[0] - 1)
            col = rn.randint(0, self.grid_size[1] - 1)

            while self.grid[row][col].tile_type == 'station':
                row = rn.randint(0, self.grid_size[0] - 1)
                col = rn.randint(0, self.grid_size[1] - 1)

            self.grid[row][col].tile_type = 'station'
            self.grid[row][col].coordinates = [row, col]
            self.stations_list.append(self.grid[row][col])

    def link_stations(self):
        for station in self.stations_list:

            if not station.is_linked:
                # TODO: multiple links (later)
                # number_of_links = rn.randint(1, int(len(self.stations_list) / 4))
                # for j in range(number_of_links):

                to_link = self.stations_list[rn.randint(0, len(self.stations_list) - 1)]

                while to_link == station:
                    to_link = self.stations_list[rn.randint(0, len(self.stations_list) - 1)]

                # if abs(to_link.coordinates[0] - station.coordinates[0]) == 1:
                #     breakpoint()

                if station.coordinates[0] < to_link.coordinates[0]:
                    for i in range(station.coordinates[0] + 1, to_link.coordinates[0] + 2):
                        station.paths_to_other_station.append((i, station.coordinates[1] + 1))

                else:
                    for i in range(station.coordinates[0] + 1, to_link.coordinates[0], -1):
                        station.paths_to_other_station.append((i, station.coordinates[1] + 1))

                if station.coordinates[1] < to_link.coordinates[1]:
                    for i in range(station.coordinates[1] + 1, to_link.coordinates[1] + 2):
                        station.paths_to_other_station.append((to_link.coordinates[0] + 1, i))

                else:
                    for i in range(station.coordinates[1] + 1, to_link.coordinates[1], -1):
                        station.paths_to_other_station.append((to_link.coordinates[0] + 1, i))

                station.is_linked = True
                to_link.is_linked = True

        print(self.stations_list[0].paths_to_other_station)



    def generate_random_metro(self):
        self.initialise()
        self.generate_stations()
        self.link_stations()