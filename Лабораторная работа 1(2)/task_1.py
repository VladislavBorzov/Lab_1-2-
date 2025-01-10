# TODO Написать 3 класса с документацией и аннотацией типов
class Jacket:
    """Абстрактный класс для описания пиджака"""

    def __init__(self, size: float, material: str, color: str):
        """
        Конструктор класса Jacket.

        :param size: Размер пиджака (в числовом формате)
        :type size: float
        :param material: Материал, из которого сделан пиджак
        :type material: str
        :param color: Цвет пиджака
        :type color: str
        """
        if size <= 0 or size > 100:
            raise ValueError("Размер пиджака должен быть положительным числом от 0 до 100.")
        if not isinstance(material, str) or not material.strip():
            raise ValueError("Материал пиджака должен быть непустым строковым значением.")
        if not isinstance(color, str) or not color.strip():
            raise ValueError("Цвет пиджака должен быть непустым строковым значением.")

        self.size = size
        self.material = material
        self.color = color

    def put_on(self) -> None:
        """
        Метод для надевания пиджака.

        :return: None
        """
        pass

    def take_off(self) -> None:
        """
        Метод для снятия пиджака.

        :return: None
        """
        pass

    def clean(self) -> None:
        """
        Метод для чистки пиджака.

        :return: None
        """
        pass

class Snowboard:
    """Абстрактный класс для описания сноуборда"""

    def __init__(self, length: float, width: float, stiffness: int):
        """
        Конструктор класса Snowboard.

        :param length: Длина сноуборда (в метрах)
        :type length: float
        :param width: Ширина сноуборда (в метрах)
        :type width: float
        :param stiffness: Жесткость сноуборда (целое число от 1 до 10)
        :type stiffness: int
        """
        if length <= 0:
            raise ValueError("Длина сноуборда должна быть положительной.")
        if width <= 0:
            raise ValueError("Ширина сноуборда должна быть положительной.")
        if stiffness < 1 or stiffness > 10:
            raise ValueError("Жесткость сноуборда должна быть целым числом от 1 до 10.")

        self.length = length
        self.width = width
        self.stiffness = stiffness

    def ride(self) -> None:
        """
        Метод для катания на сноуборде.

        :return: None
        """
        pass

    def wax(self) -> None:
        """
        Метод для нанесения воска на сноуборд.

        :return: None
        """
        pass

    def store(self) -> None:
        """
        Метод для хранения сноуборда.

        :return: None
        """
        pass

class Boat:
    """Абстрактный класс для описания лодки"""

    def __init__(self, length: float, capacity: int, engine_type: str):
        """
        Конструктор класса Boat.

        :param length: Длина лодки (в метрах)
        :type length: float
        :param capacity: Вместимость лодки (количество пассажиров)
        :type capacity: int
        :param engine_type: Тип двигателя лодки
        :type engine_type: str
        """
        if length <= 0:
            raise ValueError("Длина лодки должна быть положительной.")
        if capacity < 0:
            raise ValueError("Вместимость лодки должна быть неотрицательной.")
        if not isinstance(engine_type, str) or not engine_type.strip():
            raise ValueError("Тип двигателя лодки должен быть непустым строковым значением.")

        self.length = length
        self.capacity = capacity
        self.engine_type = engine_type

    def sail(self) -> None:
        """
        Метод для плавания на лодке.

        :return: None
        """
        pass

    def dock(self) -> None:
        """
        Метод для швартовки лодки.

        :return: None
        """
        pass

    def refuel(self) -> None:
        """
        Метод для заправки лодки топливом.

        :return: None
        """
        pass

if __name__ == "__main__":
    import doctest


    class TestClasses:
        """
        Тестовый класс для демонстрации работы классов.

        >>> jacket = Jacket(size=42, material="шерсть", color="синий")
        >>> snowboard = Snowboard(length=1.6, width=0.25, stiffness=7)
        >>> boat = Boat(length=8, capacity=4, engine_type="бензиновый")

        >>> jacket.put_on()
        >>> snowboard.wax()
        >>> boat.sail()
        """


    doctest.testmod()


