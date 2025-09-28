class Door:
    def __init__(self):
        self.is_locked = False

    def lock(self):
        self.is_locked = True

    def unlock(self):
        self.is_locked = False

# Нарушение принципа:
door = Door()
if door.is_locked:
    door.unlock()
else:
    door.lock()


class Door:
    def __init__(self):
        self.is_locked = False

    def switch(self):
        self.is_locked = not self.is_locked

door = Door()
door.switch()

