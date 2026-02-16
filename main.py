from ursina import *

from icecream import ic

from classes.create_objects import my_water_area, my_grid_overlay, my_lower_grid, enemy_water_area, enemy_grid_overlay, enemy_lower_grid
from classes.class_CoordinatesText import CoordinatesText

my_coordinates = CoordinatesText(my_lower_grid)
enemy_coordinates = CoordinatesText(enemy_lower_grid)

from classes.class_NavButton import NavButton

nav_button = NavButton()


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

