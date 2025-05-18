import random


def print_maze(maze):
    """Функция для вывода лабиринта"""
    for row in maze:
        print("".join(row))


def move_snake(snake, direction):
    """Функция для перемещения змеи"""
    head = snake[-1]
    if direction == 'up':
        new_head = [head[0] - 1, head[1]]
    elif direction == 'down':
        new_head = [head[0] + 1, head[1]]
    elif direction == 'left':
        new_head = [head[0], head[1] - 1]
    elif direction == 'right':
        new_head = [head[0], head[1] + 1]
    else:
        raise ValueError(f"Неправильное направление: {direction}")
    return new_head


def is_valid_move(new_head, maze, exit_position):
    """Проверяет, является ли новый ход допустимым"""
    num_rows = len(maze)
    num_cols = len(maze[0])
    if new_head[0] < 0 or new_head[0] >= num_rows:
        return False
    if new_head[1] < 0 or new_head[1] >= num_cols:
        return False
    if maze[new_head[0]][new_head[1]] == '#' or maze[new_head[0]][new_head[1]] == '*':  # Стена или тело змеи
        return False
    # Если змея достигла выхода, возвращаем True
    if new_head == exit_position:
        return True
    return True


def generate_food(maze, snake):
    """Генерирует еду в случайном месте на карте"""
    free_cells = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == '.':
                free_cells.append((i, j))

    food_pos = random.choice(free_cells)
    maze[food_pos[0]][food_pos[1]] = '$'  # Еда обозначается как $
    return food_pos


def check_eat_food(head, food_pos):
    """Проверяет, съела ли змея еду"""
    return head == food_pos


def update_snake(snake, new_head, ate_food=False):
    """Обновляет позицию змеи"""
    snake.append(new_head)
    if not ate_food:
        del snake[0]


def main():
    # Лабиринт
    maze = [
        ['#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#', '#'],
        ['#', '.', '#', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '#'],
        ['#', '.', '#', '.', '.', '#'],
        ['#', '.', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '.'],
        ['#', '#', '#', '#', '#', '#']
    ]

    # Начальные координаты выхода
    exit_position = [7, 5]

    # Помечаем начальный выход в лабиринте
    maze[exit_position[0]][exit_position[1]] = '&'

    # Начальная позиция змеи
    snake = [[2, 3], [2, 4]]

    # Генерация первой еды
    food_pos = generate_food(maze, snake)


    while True:
        # Выводим лабиринт с текущей позицией змеи
        for pos in snake:
            maze[pos[0]][pos[1]] = '*'  # Змея обозначается как *
        maze[snake[-1][0]][snake[-1][1]] = '@'  # Голова змеи обозначается как @
        print_maze(maze)

        # Сбрасываем символы змеи после отображения
        for pos in snake:
            maze[pos[0]][pos[1]] = '.'

        # Восстанавливаем символ выхода
        maze[exit_position[0]][exit_position[1]] = '&'

        # Получение направления движения от пользователя
        direction = input("Введите направление (w/a/s/d): ").lower()
        if direction not in {'w', 'a', 's', 'd'}:
            print("Неверное направление!")
            continue

        # Преобразование ввода в направление
        directions = {
            'w': 'up',
            'a': 'left',
            's': 'down',
            'd': 'right'
        }
        direction = directions.get(direction)

        # Перемещение головы змеи
        new_head = move_snake(snake, direction)

        # Проверяем, возможен ли этот ход
        if not is_valid_move(new_head, maze, exit_position):
            if new_head == exit_position and eaten_food_count > 0:
                print("Поздравляю! Вы нашли выход из лабиринта!")
                break
            else:
                print("Вы столкнулись со стеной или своим телом! Игра окончена.")
                break

        # Проверяем, съела ли змея еду
        ate_food = check_eat_food(new_head, food_pos)

        if ate_food:
            eaten_food_count += 1
            food_pos = generate_food(maze, snake)  # Генерируем новую еду

        # Обновление змеи
        update_snake(snake, new_head, ate_food)

        # Пауза перед следующим ходом
        input("Нажмите Enter для следующего хода...")

        # Вывод поздравленя с победой
        if new_head == exit_position and eaten_food_count > 0:
            print("Поздравляю! Вы нашли выход из лабиринта!")
            break

        # Если игрок достиг выхода, но не съел ни одного куска еды
        if new_head == exit_position and eaten_food_count == 0:
            print("Вы достигли выхода, но не съели ни одного куска еды. Проигрыш!")
            break


if __name__ == "__main__":
    main()