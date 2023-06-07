class InstantiateCSVError(Exception):
    """
    Класс - исключение, если item.csv поврежден (например, отсутствует одна из колонок данных)
    """
    def __init__(self):
        self.massage = "Поврежден файл"

    def __str__(self):
        return self.massage
