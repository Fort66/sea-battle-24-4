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

        self.on_click = self.move_camera
        self.old_coordinates = camera.position


    def move_camera(self):
        if camera.position != Vec3(-30, 0, 0):
            camera.position -= Vec3(1, 0, 0)








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