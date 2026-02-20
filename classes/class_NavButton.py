from ursina import Entity, Button, color, camera, Vec3, time


class NavButton(Button):
    def __init__(self,
                text='Click',
                position=(0, .4, 0),
                scale=.1,
                color=color.blue,
                **kwargs):
        super().__init__(
            text=text,
            scale=scale,
            color=color,
            position=position,
        )

        self.enemy_position = False
        self.on_click = self.change_value


    def change_value(self):
        self.enemy_position = not self.enemy_position








# def on_button_click():
#     print('Button clicked!')

# button = Button(
#     text='Click me',
#     position=(0, 0, 0),
#     scale=(.2, .1, .2),
#     color=color.blue,
#     background_color=color.black,
#     on_click=on_button_click,
#     border_color=color.white,
# )