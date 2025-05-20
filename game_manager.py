class GameManager:
    def __init__(self):
        self.current_scene = 0

    def change_scene(self, next_scene):
        self.current_scene = next_scene