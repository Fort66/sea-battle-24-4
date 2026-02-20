from .class_Ships import Ships


class ShipsCreator:
    __inctance = None

    def __new__(cls, *args, **kwargs):
        if cls.__inctance is None:
            cls.__inctance = super().__new__(cls, *args, **kwargs)
        return cls.__inctance

    def __init__(self, water=None):
        self.water = water
        self.create_ship_command = False
        self.deck_amount = 0
        self.model = None
        self.texture = None
        self.ship = []

    def update(self):
        if self.create_ship_command:
            self.ship.append(
                Ships(
                    self.model,
                    self.texture,
                    scale=.015,
                    position=self.water.map_position_cells[(0, 0)],
                    deck_amount=self.deck_amount
                )
            )

            self.create_ship_command = False
            self.deck_amount = 0
            self.model = None
            self.texture = None
