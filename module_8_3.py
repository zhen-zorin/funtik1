

class Car:
    def __init__(self, model: str, vin: int, nambers: str):
        self.model = model # Название автомобиля
        if self.__is_valid_vin(vin):
            self.__vin = vin # Вин номер атомобиля
        if self.__is_valid_nambers(nambers):
            self.__nambers = nambers # Номер автомобиля (строка)

    def __is_valid_vin(self, vin_nanber):
        if not isinstance(vin_nanber, int):
            raise IncorrectVinNamber('Некорректный тип vin номер')
        elif not 1000000 <= vin_nanber <= 9999999:
            raise IncorrectVinNamber('Некорректный диапазон для vin номера')
        else:
            return True

    def __is_valid_nambers(self, nambers):
        if not isinstance(nambers, str):
            raise IncorrectCarNambers('Некорректный тип данных для номеров')
        elif len(nambers) != 6:
            raise IncorrectCarNambers('Некорректная длинна номера')
        else:
            return True

class IncorrectVinNamber(Exception):
    def __init__(self, message):
        self.message =message

class IncorrectCarNambers(Exception):
    def __init__(self, message):
        self.message = message

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNamber as exc:
    print(exc.message)
except IncorrectCarNambers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')
try:
    second = Car('Model2', 300, 't001tp')
except IncorrectVinNamber as exc:
    print(exc.message)
except IncorrectCarNambers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')
try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNamber as exc:
    print(exc.message)
except IncorrectCarNambers as exc:
    print(exc.message)
else:
    print(f'{third. model} успешно создан')