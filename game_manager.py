class GameManager:
    def __init__(self):
        self.current_scene = 0
        self.lives = 3
        self.previous_choices = []

    def change_scene(self, next_scene):
        """Переходит к следующей сцене"""
        self.previous_choices.append(self.current_scene)
        self.current_scene = next_scene

    def lose_life(self):
        """Уменьшает количество жизней игрока."""
        self.lives -= 1
        return self.lives <= 0