from ursina import Entity, Vec3, mouse

from .class_ShipsCreator import ShipsCreator

ships_creator = ShipsCreator()

class ShipsMenu(Entity):
    def __init__(self,
                water=None,
                model=None,
                texture=None,
                scale=1,
                rotation=Vec3(0, 0, 0),
                position=Vec3(0, 0, 0),
                deck_amount=0,
                ship_counter=0,
                ):

        super().__init__(
            model=model,
            texture=texture,
            scale=scale,
            rotation=rotation,
            position=position,
            collider='box'
        )

        self.water = water
        self.model = model
        self.texture = texture
        self.scale = scale
        self.rotation = rotation
        self.position = position
        self.deck_amount = deck_amount
        self.ship_counter = ship_counter

    def input(self, key):
        if key == 'left mouse down' and mouse.hovered_entity == self:
            self.ship_counter -= 1
            ships_creator.deck_amount = self.deck_amount
            ships_creator.create_ship_command = True
            ships_creator.model = self.model.name
            ships_creator.texture = self.texture
            ships_creator.water = self.water

        if self.ship_counter <= 0:
            self.visible = False