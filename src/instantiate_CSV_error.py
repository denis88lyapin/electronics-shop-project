class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        if args