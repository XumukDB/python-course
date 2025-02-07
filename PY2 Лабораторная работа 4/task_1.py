POT_DIAMETER = 20  # диаметр кастрюли


class Macaroni:
    """
        Базовый класс макарошек.
        Объекты - пачки макаронных изделий, характеризующиеся названием, весом и временем приготовления.

        Атрибуты
        name: бренд производителя
        weight: вес в граммах
        cooking_time: рекомендуемое время приготовления

        Методы
        change_remaining_weight(new_weight): изменяет вес оставшихся макарон в пачке
        cook(weight): готовит заданное количество макарон
    """

    def __init__(self, name: str, weight: int, cooking_time: int):
        """
            Создание и подготовка к работе объекта "Пачка макарошек"

            :param name: бренд производителя
            :param weight: вес в граммах
            :param cooking_time: рекомендуемое время приготовления

            Пример:
            >>> Pachka1 = Macaroni("Barilla", 400, 11)
        """
        self.name = name
        self.weight = weight
        self.cooking_time = cooking_time

    @property  # все атрибуты прописываем в свойства, чтобы любое изменение проходило через проверки
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        self._name = name

    @property
    def weight(self) -> int:
        return self._weight
    @weight.setter
    def weight(self, weight: int) -> None:
        if not isinstance(weight, int):
            raise TypeError("Вес макарошек в пачке должен быть типа int")
        if weight < 0:
            raise ValueError("Вес не может быть отрицательным")
        self._weight = weight

    @property
    def cooking_time(self) -> int:
        return self._cooking_time
    @cooking_time.setter
    def cooking_time(self, cooking_time: int) -> None:
        if not isinstance(cooking_time, int):
            raise TypeError("Время приготовления должно быть типа int")
        if cooking_time <= 0:
            raise ValueError("Время приготовления должно быть положительным")
        self._cooking_time = cooking_time

    def __str__(self):
        return f"Пачка макарон {self.name}. Вес {self.weight} грамм. Время приготовления {self.cooking_time} минут."

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight!r},"
                f" cooking_time={self.cooking_time!r})")

    def change_remaining_weight(self, new_weight: int) -> None:
        """
            Изменение веса оставшихся макарон в пачке
            :param new_weight: новое значение веса
        """
        self.weight = new_weight

    def cook(self, weight: int) -> None:
        """
            Приготовить заданное количество макарон
            :param weight: сколько грамм макарон приготовить
            :raise ValueError: если столько макарон в пачке нет.
        """
        if weight > self.weight:
            raise ValueError(f"Не удастся приготовить {weight} грамм, в пачке осталось {self.weight}")
        ...


class Spaghetti(Macaroni):
    """
        Спагетти - дочерний класс макарошек
        Объекты - пачки спагетти, характеризующиеся названием, весом, временем приготовления и длиной.

        Атрибуты
        name: бренд производителя
        weight: вес в граммах
        cooking_time: рекомендуемое время приготовления
        length: длина спагетти

        Методы
        change_remaining_weight(new_weight): изменяет вес оставшихся спагетти в пачке
        cook(weight): готовит заданное количество спагетти
    """

    def __init__(self, name: str, weight: int, cooking_time: int, length: float):
        """
             Создание и подготовка к работе объекта "Пачка спагетти"

             :param name: бренд производителя
             :param weight: вес в граммах
             :param cooking_time: рекомендуемое время приготовления
             :param length: длина спагетти

             Примеры:
             >>> Pachka2 = Spaghetti("Federici", 450, 9, 26.0)
        """
        super().__init__(name=name, weight=weight, cooking_time=cooking_time)
        self.length = length

    @property
    def length(self) -> float:
        return self._length
    @length.setter
    def length(self, length: float) -> None:
        if not isinstance(length, float):
            raise TypeError("Длина спагетти должна быть типа float")
        if length <= 0:
            raise ValueError("Длина спагетти должна быть положительной")
        self._length = length

    def __str__(self):
        return (f"Пачка спагетти {self.name}. Вес {self.weight} грамм. Время приготовления {self.cooking_time} минут."
                f" Длина {self.length}")

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight!r},"
                f" cooking_time={self.cooking_time!r}, length={self.length!r})")

    def cook(self, weight: int) -> None:
        """ Перегружаем метод, поскольку спагетти возможно не влезут в кастрюлю """
        if weight > self.weight:
            raise ValueError(f"Не удастся приготовить {weight} грамм, в пачке осталось {self.weight}")
        if self.length > POT_DIAMETER:
            self.length /= 2  # ломаем слишком длинные спагетти пополам перед приготовлением
        super().cook(weight)  # дальше готовим как обычно


class Vermicelli(Macaroni):
    """
        Вермишель - дочерний класс макарошек
        Объекты - пачки вермишели, характеризующиеся названием, весом и временем приготовления.

        Атрибуты
        name: бренд производителя
        weight: вес в граммах
        cooking_time: рекомендуемое время приготовления

        Методы
        change_remaining_weight(new_weight): изменяет вес оставшейся вермишели в пачке
        cook(weight): готовит заданное количество вермишели
        cook_by_pan(weight): готовит заданное количество вермишели на сковороде
    """

    def __str__(self):
        return f"Пачка вермишели {self.name}. Вес {self.weight} грамм. Время приготовления {self.cooking_time} минут."

    def cook_by_pan(self, weight: int) -> None:
        """
            Приготовить указанное количество на сковороде, предварительно обжарив
            :param weight: сколько грамм макарон приготовить

            Пример:
             >>> Pachka3 = Vermicelli("Makfa", 450, 2)
             >>> Pachka3.cook_by_pan(200)
        """


if __name__ == "__main__":
    pass
