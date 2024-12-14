import doctest
from datetime import datetime


class Lecture:
    def __init__(self, subject: str, speaker: str, date: datetime, classroom: int):
        """
        Создание и подготовка к работе объекта "Лекция"

        :param subject: Тема лекции
        :param speaker: ФИО лектора
        :param date: дата проведения
        :param classroom: номер аудитории

        Примеры:
        >>> Calculus01 = Lecture("Введение в математический анализ", "Колмогоров А. Н.", datetime(2025, 2, 14, 13, 15), 201)
        """
        self.subject = subject
        self.speaker = speaker

        if not isinstance(date, datetime):
            raise TypeError("Дата и время должны быть указаны в формате datetime")
        self.date = date

        if not isinstance(classroom, int):
            raise TypeError("Номер аудитории должен быть int")
        if classroom < 0 or classroom > 516:
            raise ValueError("Аудитории с таким номером нет")
        self.classroom = classroom

    def is_happened(self) -> bool:
        """
        Функция проверяет прошло ли назначенное время лекции

        :return: Наступила ли дата проведения

        Примеры:
        >>> Econometrics12 = Lecture("Итоговый тест", "Подкорытова О. А.", datetime(2024, 12, 6, 13, 15), 36)
        >>> Econometrics12.is_happened()
        """

    def change_classroom(self, new_classroom: int) -> None:
        """
        Меняет место проведения на указанное
        :param new_classroom: новое место проведения

        :raise ValueError: Если адитории с указанным номером нет, возвращается ошибка.

        Примеры:
        >>> Econometrics12 = Lecture("Итоговый тест", "Подкорытова О. А.", datetime(2024, 12, 6, 13, 15), 36)
        >>> Econometrics12.change_classroom(93)
        """
        if not isinstance(new_classroom, int):
            raise TypeError("Номер аудитории должен быть int")
        if new_classroom < 0 or new_classroom > 516:
            raise ValueError("Аудитории с таким номером нет")
        self.classroom = new_classroom


class Table:
    def __init__(self, material: str, items: list[str]):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал столешницы
        :param items: список предметов на столе

        Примеры:
        >>> LivingRoomTable = Table("Дерево", ["Книга","Кружка кофе","Ежедневник"])
        """
        self.material = material
        self.items = items

    def put_items(self, new_items : list[str]) -> None:
        """
        Функция добавляет предметы на стол

        :param new_items: новые предметы

        Примеры:
        >>> KitchenTable = Table("Стекло", ["Тарелка","Нож"])
        >>> KitchenTable.put_items(["Яблоко", "Прихватка"])
        """

    def flip(self) -> None:
        """
        Переворачивает стол и все предметы падают

        Примеры:
        >>> LivingRoomTable = Table("Дерево", ["Книга","Кружка кофе","Ежедневник"])
        >>> LivingRoomTable.flip()
        """


class Boardgame:
    def __init__(self, title: str, player_count: tuple[int, int], time_to_play: int, time_per_player: bool = False,
                 personal_score: int = None):
        """
        Создание и подготовка к работе объекта "Настольная игра"

        :param title: название
        :param player_count: допустимое количество игроков в формате кортежа из двух целых чисел, где на первом месте
        минимальное количество, на втором - максимальное
        :param time_to_play: ожидаемое время партии в минутах
        :param time_per_player: True, если ожидаемое время партии указано в расчете на одного игрока
        :param personal_score: личная оценка игры в диапазоне от 1 до 10, None если оценки нет

        Примеры:
        >>> Dominion = Boardgame(title="Доминион", player_count=(2,4), time_to_play=15, time_per_player=True)
        """
        self.title = title

        if not isinstance(player_count, tuple):
            raise TypeError("Число игроков должно быть в формате кортежа из двух целых чисел, где на первом месте \
            минимальное количество, на втором - максимальное")
        if len(player_count) != 2:
            raise TypeError("Количество элементов в кортеже не равно двум")
        if not isinstance(player_count[0], int) or not isinstance(player_count[1], int):
            raise TypeError("Не все элементы кортежа целочисленны")
        if player_count[0] < 1:
            raise ValueError("Минимальное число игроков не может быть меньше 1")
        if player_count[0] > player_count[1]:
            raise ValueError("Минимальное число игроков не может быть больше максимального")
        self.playerCount = player_count

        if not isinstance(time_to_play, int):
            raise TypeError("Время партии должно быть указано целым количеством минут")
        if time_to_play <= 0:
            raise ValueError("Время партии должно быть положительным")
        self.timeToPlay = time_to_play

        if not isinstance(time_per_player, bool):
            time_per_player = True  # если в необязательный аргумент что-то передано, будем считать значение истинным
        self.timePerPlayer = time_per_player

        if not isinstance(personal_score, int) and not isinstance(personal_score, type(None)):
            raise TypeError("Оценка должна быть в формате целого числа, либо None")
        if isinstance(personal_score, int) and (personal_score < 1 or personal_score > 10):
            raise ValueError("Оценка должна быть в диапазоне от 1 до 10")
        self.personal_score = personal_score

    def can_be_played(self, players: int, available_time: int) -> int:
        """
        Функция проверяет, может ли игра быть сыграна данным составом за определенное время, если да, возвращает
        количество партий

        :return: Ожидаемое количество партий

        Примеры:
        >>> Nemesis = Boardgame("Немезида", (1, 5), 210)
        >>> Nemesis.can_be_played(players=4, available_time=300)
        """

    def rate(self, new_score: int) -> None:
        """
        Устанавливает оценку на указанную
        :param new_score: новая оценка целым числом в диапазоне от 1 до 10

        :raise ValueError: Если оценка вне указанного диапазона, возвращается ошибка.

        Примеры:
        >>> TicTacToe = Boardgame("Крестики нолики", (2, 2), 1)
        >>> TicTacToe.rate(1)
        """
        if not isinstance(new_score, int):
            raise TypeError("Оценка должна быть в формате целого числа")
        if new_score < 1 or new_score > 10:
            raise ValueError("Оценка должна быть в диапазоне от 1 до 10")
        self.personal_score = new_score

    def remove_score(self) -> None:
        """
        Убирает оценку игре, устанавливая значение None

        Примеры:
        >>> Coup = Boardgame("Переворот", (3, 6), time_to_play=3, time_per_player=True, personal_score=7)
        >>> Coup.remove_score()
        """
        self.personal_score = None


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
