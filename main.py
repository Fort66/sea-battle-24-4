from ursina import *

from icecream import ic

from string import ascii_letters

from classes.class_SeaPlane import SeaPlane
from classes.class_GridOverlay import GridOverlay

from classes.class_CoordinatesText import CoordinatesText


sea_plane = SeaPlane()
grid_overlay = GridOverlay(10, 10, position=Vec3(0, .002, 0))
lower_grid = GridOverlay(12, 12, color=color.rgba(0, 0, 0, .1), position=Vec3(0, -.002, 0))


letters_list = [ascii_letters[i] for i in range(10)]
digits_list = [str(i) for i in range(1, 11)]

for i in range(1, 11):
    CoordinatesText(
        model=Text(
            text=letters_list[i - 1],
            color=color.white,
        ),
        scale=20,
        rotation=Vec3(90, 0, 0),
    ).position = lower_grid.map_position_cells[(i, 11)]

    CoordinatesText(
        model=Text(
            text=letters_list[i - 1],
            color=color.white,
        ),
        scale=20,
        rotation=Vec3(90, 0, 0),
    ).position = lower_grid.map_position_cells[(i, 0)]

    CoordinatesText(
        model=Text(
            text=digits_list[i - 1],
            color=color.white,
        ),
        scale=20,
        rotation=Vec3(90, 0, 0),
    ).position = lower_grid.map_position_cells[(11, i)]

    CoordinatesText(
        model=Text(
            text=digits_list[i - 1],
            color=color.white,
        ),
        scale=20,
        rotation=Vec3(90, 0, 0),
    ).position = lower_grid.map_position_cells[(0, i)]



if __name__ == "__main__":
    window.vsync = False
    app = Ursina()

    ambient_lights = AmbientLight(color=color.yellow)


    def update():
        pass


    EditorCamera()
    camera.position = Vec3(0, 15, 0)
    camera.rotation = Vec3(35, 0, 0)
    camera.fov = 60


    app.run()

