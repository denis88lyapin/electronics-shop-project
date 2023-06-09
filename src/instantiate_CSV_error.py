class InstantiateCSVError(Exception):
    """
    Класс - исключение, если item.csv поврежден (например, отсутствует одна из колонок данных)
    """
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message
