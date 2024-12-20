import random#Здесь мы импортируем модуль random который позволяет генерировать случайные числа для размещения кораблей


class SeaBattle:
    def __init__(self):# функция аницализации классов
        self.size = 10  # Размер поля 10x10
        self.field = [['.' for _ in range(self.size)] for _ in range(self.size)]#это мы типо ставим точки на пустые ячейки
        self.ships = []  # Список для хранения кораблей
        self.ship_types = { #Символ { используется в Python для обозначения начала словаря
            4: 1,  # 1 четырехпалубный корабль
            3: 2,  # 2 трехпалубных корабля
            2: 3,  # 3 двухпалубных корабля
            1: 4  # 4 однопалубных корабля
        }
        self.place_ships()#размещаем все корабли на поле

    def print_field(self, reveal=False):#Метод print_field отвечает за отображение игрового поля.
        print("  " + " ".join(letter for letter in 'АБВГДЕЖЗИЙ'))  # Заголовок столбцов
        for i in range(self.size):
            row_label = i + 1
            if reveal:
                print(row_label, " ".join(self.field[i]))  # Показываем все поля, если reveal=True
            else:
                print(row_label, " ".join(['.' if cell == 'S' else cell for cell in self.field[i]]))# Скрываем корабли
                else:


    def place_ships(self):#Метод place_ships отвечает за размещение кораблей на поле.
        for size, count in self.ship_types.items():#для каждого корабля из self.ship_types он вызывает метод place ship столькоо раз(тип сколько кораблей быть)
            for _ in range(count):
                self.place_ship(size)#столькоо раз(тип сколько кораблей быть)

    def place_ship(self, size):#Метод place_ship размещает один корабль на поле, проверяя, может ли он быть размещен в выбранном месте.
        placed = False
        while not placed:
            orientation = random.choice(['H', 'V'])  # Горизонтально или вертикально
            if orientation == 'H':
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - size)  # Убедимся, что корабль помещается
                if self.check_space(row, col, size, orientation):
                    for i in range(size):
                        self.field[row][col + i] = 'S'  # 'S' означает наличие корабля
                    self.ships.append(((row, col), orientation, size))
                    placed = True
            else:  # Вертикально
                row = random.randint(0, self.size - size)  # Убедимся, что корабль помещается
                col = random.randint(0, self.size - 1)
                if self.check_space(row, col, size, orientation):
                    for i in range(size):
                        self.field[row + i][col] = 'S'
                    self.ships.append(((row, col), orientation, size))
                    placed = True

    def check_space(self, row, col, size, orientation):#Метод check_space проверяет, можно ли разместить корабль в заданной позиции.
        if orientation == 'H':
            for i in range(size):
                if self.field[row][col + i] == 'S':  # Если корабль уже стоит
                    return False
                # Проверка соседних клеток
                if row > 0 and self.field[row - 1][col + i] == 'S':  # Сверху
                    return False
                if row < self.size - 1 and self.field[row + 1][col + i] == 'S':  # Снизу
                    return False
                if col > 0 and self.field[row][col + i - 1] == 'S':  # Слева
                    return False
                if col + i < self.size - 1 and self.field[row][col + i + 1] == 'S':  # Справа
                    return False
        else:  # Вертикально
            for i in range(size):
                if self.field[row + i][col] == 'S':  # Если корабль уже стоит
                    return False
                # Проверка соседних клеток
                if col > 0 and self.field[row + i][col - 1] == 'S':  # Слева
                    return False
                if col < self.size - 1 and self.field[row + i][col + 1] == 'S':  # Справа
                    return False
                if row > 0 and self.field[row + i - 1][col] == 'S':  # Сверху
                    return False
                if row + i < self.size - 1 and self.field[row + i + 1][col] == 'S':  # Снизу
                    return False
        return True

    def shoot(self, coordinate):#Метод shoot обрабатывает выстрел по заданным координатам.
        row, col = self.convert_coordinate(coordinate)#Сначала координаты преобразуются с помощью метода convert_coordinate.
        if self.field[row][col] == 'S':
            self.field[row][col] = 'X'  # X означает попадание
            print("Попадание!")
            self.ships = [ship for ship in self.ships if not self.is_sunk(ship)]
        else:
            self.field[row][col] = 'O'  # O означает промах
            print("Промах!")
#(Если в клетке есть корабль ('S'), она заменяется на 'X' и выводится сообщение "Попадание". Если нет — на 'O' и выводится сообщение "Промах".)
    def convert_coordinate(self, coordinate):#Метод convert_coordinate преобразует координаты, введенные пользователем (например, 'А1'), в индексы, которые использует программа.
        row = ord(coordinate[0]) - ord('А')  # Переводим букву в индекс строки
        col = int(coordinate[1:]) - 1  # Переводим номер столбца в индекс
        return row, col

    def is_sunk(self, ship):#Метод is_sunk проверяет, потоплен ли корабль.
        (start, orientation, size) = ship
        if orientation == 'H':
            return all(self.field[start[0]][start[1] + i] == 'X' for i in range(size))
        else:
            return all(self.field[start[0] + i][start[1]] == 'X' for i in range(size))


def main():#В функции main() начинается игра: создается экземпляр SeaBattle, печатается поле и предоставляется пользователю возможность вводить координаты.
    game = SeaBattle()
    game.print_field()  # Печатаем игровое поле скрыто
    print("Вводите координаты на примере 'А1' для стрельбы.")

    while True:
        coordinate = input("Введите координаты для стрельбы (или 'exit' для выхода): ")
        if coordinate.lower() == 'exit':
            break
        if len(coordinate) < 2 or len(coordinate) > 3:
            print("Некорректный ввод. Попробуйте еще раз.")
            continue
        try:
            game.shoot(coordinate)
            game.print_field()  # Печатаем поле после каждого выстрела
        except IndexError:
            print("Выход за границы поля. Попробуйте еще раз.")
        except Exception as e:
            print(f"Произошла ошибка: {e}. Попробуйте еще раз.")


if __name__ == "__main__":#Этот блок позволяет запустить игру, если скрипт выполняется как основной. При этом вызывается основная функция main().
    main()
