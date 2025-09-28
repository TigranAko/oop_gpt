class Config:
    def __init__(self, settings=None):
        self.settings = settings or {"debug": False, "db": "sqlite"}

    def get(self, key):
        return self.settings.get(key)  # Возвращает None, если ключа нет

class Config:
    def __init__(self, settings={"debug": False, "db": "sqlite"}):
        self.settings = settings 

    def get(self, key):
        return self.settings[key]

