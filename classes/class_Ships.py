from ursina import Entity, color, Vec3, mouse, scene
from ursina.prefabs.draggable import Draggable


from icecream import ic

# my_ship = Entity(
#         model='assets/models/newport/uss_newport_news_war_thunder.glb',
#         scale=.015,
#         rotation=Vec3(90, 0, 0),
#         position=Vec3(10, 0.02, 0)
#     )


# class Ships(Entity):
#     def __init__(self):
#         super().__init__(
#             model='assets/models/newport/uss_newport_news_war_thunder.glb',
#             scale=.015,
#             rotation=Vec3(90, 0, 0),
#             position=Vec3(10, 0.02, 0)
#         )


class Ships(Entity):
    def __init__(self,
                model='',
                texture='',
                scale=1,
                rotation=Vec3(0, 0, 0),
                position=Vec3(0, 0, 0)
                ):

        super().__init__(
            model=model,
            scale=scale,
            rotation=rotation,
            position=position,
            collider='box'
        )

        self.model = model
        self.texture = texture
        self.scale = scale
        self.rotation = rotation
        self.position = position

        self.is_grabbed = False

    def input(self, key):
        if key == 'left mouse down':
            if mouse.hovered_entity == self:
                self.is_grabbed = True
                ic(self.is_grabbed)
                Draggable(parent=scene, model=self,
                        plane_direction=(1,0,1), lock=(0,1,0))