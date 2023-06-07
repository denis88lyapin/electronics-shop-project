class InstantiateCSVError(Exception):
    """
    Класс - исключение, если item.csv поврежден (например, отсутствует одна из колонок данных)
    """
    def __init__(self):
        self.massage = "Файл item.csv поврежден"

    def __str__(self):
        return self.massage
