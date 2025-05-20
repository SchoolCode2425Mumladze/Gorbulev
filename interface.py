import turtle
from game_manager import GameManager
from scenes1 import scenes

BACKGROUNDS = ["dark_room_gif.gif", "light_in_the_dark_gif.gif", "strange_man_gif.gif", "forest_gif.gif", "village_gif.gif", "c.gif", "throne.gif", "halls.gif", "throne.gif"]


class Interface:
    def __init__(self, manager):
        self.manager = manager
        self.screen = turtle.Screen()
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.background_index = 0
        scene_data = scenes[self.manager.current_scene]
        if scene_data.get('change_background', False):
            self.screen.bgpic(BACKGROUNDS[self.background_index])
        else:
            self.screen.bgcolor("white")

    def display_scene(self):
        scene_data = scenes[self.manager.current_scene]
        description = scene_data["description"]
        choices = scene_data.get("choices", [])

        self.turtle.clear()
        self.turtle.penup()
        self.turtle.color("green")
        self.turtle.goto(0, 0)
        self.turtle.write(description, align="center", font=("Arial", 16, "normal"))

        y_pos = -50
        for idx, choice in enumerate(choices):
            self.turtle.goto(0, y_pos - idx * 30)
            self.turtle.write(f"{idx + 1}. {choice['text']}", align="center", font=("Arial", 14, "normal"))

        self.display_exit_button()

    def display_exit_button(self):
        self.turtle.goto(-200, 200)
        self.turtle.write("Выход (Esc)", align="left", font=("Arial", 14, "normal"))

    def handle_choice(self, choice_idx):
        next_scene = scenes[self.manager.current_scene]['choices'][choice_idx]['next_scene']
        scene_data = scenes[next_scene]

        if scene_data.get('change_background', False):
            self.background_index += 1
            self.screen.bgpic(BACKGROUNDS[self.background_index])

        self.manager.change_scene(next_scene)
        self.display_scene()

    def setup_keybindings(self):
        self.screen.onkey(lambda: self.handle_choice(0), "1")
        self.screen.onkey(lambda: self.handle_choice(1), "2")
        self.screen.onkey(lambda: self.handle_choice(2), "3")
        self.screen.onkey(turtle.bye, "Escape")
        self.screen.listen()

    def start_game(self):
        self.setup_keybindings()
        self.display_scene()
        turtle.mainloop()