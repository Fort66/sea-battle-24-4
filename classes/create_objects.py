from ursina import Text, Vec3, color


from . class_SeaPlane import SeaPlane
from . class_GridOverlay import GridOverlay
# from . class_CoordinatesText import CoordinatesText


my_water_area = SeaPlane()
my_grid_overlay = GridOverlay(10, 10, position=Vec3(0, .002, 0))
my_lower_grid = GridOverlay(12, 12, color=color.rgba(0, 0, 0, .1), position=Vec3(0, -.002, 0))



enemy_water_area = SeaPlane(position=Vec3(-30, 0, 0))
enemy_grid_overlay = GridOverlay(10, 10, position=Vec3(-30, .002, 0))
enemy_lower_grid = GridOverlay(12, 12, color=color.rgba(0, 0, 0, .1), position=Vec3(-30, -.002, 0))