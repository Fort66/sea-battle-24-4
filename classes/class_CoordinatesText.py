from ursina import Entity, Text, color, Vec3

from . create_objects import my_lower_grid


from string import ascii_letters

class CoordinatesText:
    def __init__(self, grid):
        self.letters_list = [ascii_letters[i] for i in range(10)]
        self.digits_list = [str(i) for i in range(1, 11)]
        self.grid = grid

        self.draw_coordinates()

    def draw_coordinates(self):
        for i in range(1, 11):
            Entity(
                model=Text(
                    text=self.letters_list[i - 1],
                    color=color.white,
                ),
                scale=20,
                rotation=Vec3(90, 0, 0),
            ).position = self.grid.map_position_cells[(i, 11)]

            Entity(
                model=Text(
                    text=self.letters_list[i - 1],
                    color=color.white,
                ),
                scale=20,
                rotation=Vec3(90, 0, 0),
            ).position = self.grid.map_position_cells[(i, 0)]

            Entity(
                model=Text(
                    text=self.digits_list[i - 1],
                    color=color.white,
                ),
                scale=20,
                rotation=Vec3(90, 0, 0),
            ).position = self.grid.map_position_cells[(11, i)]

            Entity(
                model=Text(
                    text=self.digits_list[i - 1],
                    color=color.white,
                ),
                scale=20,
                rotation=Vec3(90, 0, 0),
            ).position = self.grid.map_position_cells[(0, i)]

