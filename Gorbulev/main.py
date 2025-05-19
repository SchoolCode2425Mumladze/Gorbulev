from game_manager import GameManager
from interface import Interface

manager = GameManager()
interface = Interface(manager)
interface.start_game()