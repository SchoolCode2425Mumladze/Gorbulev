import turtle

# Настройка экрана
screen = turtle.Screen()
screen.title("Choice of Life: The Order Empire. Beta")
screen.bgpic("dark_room_gif.gif")

# Состояние игры
current_scene = 0
lives = 3
previous_choices = []

# Фоны сцены
backgrounds = ["light_in_the_dark_gif.gif", "srtange_man_gif.gif"]  # добавляем картинки по порядку замены

# Сцены игры
scenes = [
    {
        "description": "Вы просыпаетесь в темной комнате. На столе лежит ключ и записка.", #0
        "choices": [
            {"text": "Взять ключ", "next_scene": 1},
            {"text": "Прочитать записку", "next_scene": 2},
            {"text": "Попробовать открыть дверь", "next_scene": 3}
        ]
    },
    {
        "description": "Вы взяли ключ. Дверь открыта. Вы вышли в коридор.",#1
        "choices": [
            {"text": "Идти налево", "next_scene": 4},
            {"text": "Идти направо", "next_scene": 5}
        ]
    },
    {
        "description": "Записка говорит: 'Он здесь, сделайте то, что он хочет.'",#2
        "choices": [
            {"text": "Взять ключ", "next_scene": 1},
            {"text": "Попробовать открыть дверь", "next_scene": 3}
        ]
    },
    {
        "description": "Дверь внезапно отворилась",#3
        "choices": [
            {"text": "Войти в дверь", "next_scene": 5}
        ],
        "change_background": True  # Меняем фон после этой сцены
    },
    {
        "description": "Вы зашли в тупик",#4
        "choices": [
            {"text": "Пойти в другую сторону", "next_scene": 5},
        ]
    },
    {
        "description": "Вы идёте всё дальше по коридору. Вдруг вы как будто вошли в гиперпространство",#5
        "choices": [
            {"text": "Осмотреться", "next_scene": 6},
        ]
    },
    {
        "description": "На вас нет костюма, который вам оставил странный человек в шляпе.\n"#6
                       "Вам вдруг захотелось спать",
        "choices": [
            {"text": "Заснуть", "next_scene": 7},
            {"text": "Стараться не заснуть", "next_scene": 8},
        ],
        "change_background": True  # Меняем фон после этой сцены
    },
    {
        "description": "'Проснитесь и пойте, мистер Смит. Проснитесь и пойте.'",#7
        "choices": [
            {"text": "Проснуться", "next_scene": 9},
        ]
    },
    {
        "description": "'Итак, мы снова встретились, мистер Смит. Надеюсь вы отдохнули.'",#8
        "choices": [
            {"text": "Согласиться", "next_scene": 10},
            {"text": "Съязвить", "next_scene": 10},
        ]
    },
    {
        "description": "Нет, я не хочу сказать, что вы спите на работе. Никто не заслуживает отдыха больше вашего.'",#9
        "choices": [
            {"text": "Перебить", "next_scene": 10},
            {"text": "Продолжить слушать", "next_scene": 11},
        ]
    },
    {
        "description": "'В любом случае вас ждёт задание. Вы узнаете всё на месте'",#10
        "choices": [
            {"text": "Как скажете", "next_scene": 12},
        ]
    },
    {
        "description": "'Однако проснитесь же, мистер Смит. Проснитесь, вас снова ждут великие дела.'",#11
        "choices": [
            {"text": "Начать путешествие", "next_scene": 12},
        ]
    },
    {
        "description": "'Скажу только, что советник короля Империи Порядка хочет забрать корону себе. Помешайте этому.'",#12
        "choices": [
            {"text": "Начать путешествие", "next_scene": 13},
        ]
    },
    {
        "description": "Продолжение следует...",
        "choices": [
            {"text": "Нажмите Escape для выхода", "next_scene": 13},
        ]
    }
]


def display_scene():
    turtle.clear()

    if scenes[current_scene].get('change_background'):
        screen.bgpic(backgrounds.pop(0))

    turtle.penup()
    turtle.color("green")
    turtle.goto(0, 0)
    turtle.write(scenes[current_scene]["description"], align="center", font=("Arial", 16, "normal"))

    # Отображение жизней
    display_lives()

    for index, choice in enumerate(scenes[current_scene]["choices"]):
        turtle.goto(0, -50 - index * 30)
        turtle.write(f"{index + 1}. {choice['text']}", align="center", font=("Arial", 14, "normal"))

    # Кнопка выхода
    display_exit_button()


def display_lives():
    turtle.goto(200, 200)
    turtle.write(f"Жизни: {lives}", align="right", font=("Arial", 14, "normal"))


def display_exit_button():
    turtle.goto(-200, 200)
    turtle.write("Выход (Esc)", align="left", font=("Arial", 14, "normal"))


def choose(choice_index):
    global current_scene
    previous_choices.append(current_scene)
    current_scene = scenes[current_scene]["choices"][choice_index]["next_scene"]
    display_scene()


def reset_game():
    global current_scene, lives, previous_choices
    lives -= 1
    if lives > 0:
        current_scene = 0
        previous_choices = []
        display_scene()
    else:
        turtle.clear()
        turtle.goto(0, 0)
        turtle.write("Все события имеют последствия.", align="center", font=("Arial", 16, "normal"))


# Обработка нажатий клавиш
def key_press_1():
    choose(0)


def key_press_2():
    choose(1)


def key_press_3():
    choose(2)


def exit_game():
    turtle.bye()  # Закрывает окно игры


# Настройка клавиш
turtle.listen()
turtle.onkey(key_press_1, "1")
turtle.onkey(key_press_2, "2")
turtle.onkey(key_press_3, "3")
turtle.onkey(exit_game, "Escape")  # Выход при нажатии Esc

# Начальная сцена
display_scene()
turtle.done()
# последовательности 311, 2211 вызывают ошибки
# также не выводится третий фон