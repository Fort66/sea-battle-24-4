from ursina import Entity, color, Vec3


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
            position=position
        )