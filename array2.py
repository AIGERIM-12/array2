import os

# Очистка экрана
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Словарь для преобразования букв в индексы столбцов
letters_to_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}

# Функция для запуска одной игры
def play_game():
    # Игровое поле 7x7
    board = [['~' for _ in range(7)] for _ in range(7)]

    # Ставим корабль из 3 клеток (горизонтально) в строке 2, начиная с колонки 2
    ship = [(1, 1), (1, 2), (1, 3)]  # Корабль состоит из 3 клеток

    # Счётчик выстрелов
    shots = 0
    shot_positions = set()  # Множество для хранения выстреленных позиций

    # Приветствие
    print("Добро пожаловать в игру 'Морской бой'!")
    name = input("Как вас зовут, игрок? ")

    while True:
        clear_screen()

        # Печатаем игровое поле
        print("   A B C D E F G")
        print("  ---------------")
        for row in range(7):
            print(f"{row+1} | {' '.join(board[row])}")

        print(f"Выстрелов: {shots}")

        # Ввод координат выстрела
        shot = input("Введите координаты для выстрела (например, A1): ").strip().upper()

        # Проверка на правильность ввода
        if len(shot) != 2 or shot[0] not in letters_to_index or not shot[1].isdigit():
            print("Неверный формат ввода. Попробуйте снова!")
            continue
        
        col = letters_to_index[shot[0]]  # Преобразуем букву в индекс столбца
        row = int(shot[1]) - 1  # Преобразуем цифру в индекс строки

        # Проверка на правильность координат (в пределах поля)
        if not (0 <= row <= 6 and 0 <= col <= 6):
            print("Координаты вне поля. Попробуйте снова!")
            continue

        # Проверка, был ли уже выстрел в эту клетку
        if (row, col) in shot_positions:
            print("Вы уже стреляли в эту клетку. Попробуйте снова!")
            continue

        # Увеличиваем счётчик выстрелов
        shots += 1
        shot_positions.add((row, col))  # Добавляем позицию в множество выстреленных клеток

        # Проверка попадания
        if (row, col) in ship:
            print("Попадание!")
            board[row][col] = 'X'  # Отметим попадание
            ship.remove((row, col))  # Удалим часть корабля
        else:
            print("Промах!")
            board[row][col] = '*'  # Отметим промах

        # Проверка на победу (если все части корабля потоплены)
        if len(ship) == 0:
            clear_screen()
            print("   A B C D E F G")
            print("  ---------------")
            for row in range(7):
                print(f"{row+1} | {' '.join(board[row])}")
            
            print(f"Поздравляем, {name}! Вы потопили корабль за {shots} выстрелов.")
            return name, shots  # Возвращаем имя игрока и количество выстрелов

        # Ожидаем нажатия Enter перед следующим ходом
        input("Нажмите Enter, чтобы продолжить...")

# Главная программа
def main():
    players_scores = []  # Список для хранения результатов игроков

    while True:
        # Запускаем одну игру
        name, shots = play_game()
        
        # Добавляем результат в список
        players_scores.append((name, shots))

        # Спрашиваем игрока, хочет ли он сыграть снова
        play_again = input("Хотите сыграть еще раз? (y/n): ").strip().lower()
        if play_again != 'y':
            # Сортируем игроков по количеству выстрелов (от лучшего к худшему)
            sorted_players = sorted(players_scores, key=lambda x: x[1])

            # Выводим таблицу результатов
            print("\nРейтинг игроков (от лучшего к худшему):")
            for idx, (player, score) in enumerate(sorted_players, 1):
                print(f"{idx}. {player} - {score} выстрелов")

            print("\nСпасибо за игру!")
            break  # Завершаем программу

# Запуск главной программы
if __name__ == "__main__":
    main()


