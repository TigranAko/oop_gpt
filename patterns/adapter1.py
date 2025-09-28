#Реализовать класс OldMusicPlayer, у которого есть метод play_jack(), возвращающий "Playing music via 3.5mm Jack".

#Реализовать класс BluetoothSpeaker, у которого есть метод play_bluetooth(), возвращающий "Playing music via Bluetooth".

#Создать класс-адаптер JackToBluetoothAdapter, который позволит старому плееру работать с BluetoothSpeaker.

#Продемонстрировать использование адаптера.

class OldMusicPlayer:
    def play_jack(self):
        return "Playing music via 3.5mm Jack"


class BluetoothSpeaker:
    def play_bluetooth(self):
        return "Playing music via 3.5mm Jack"

class JackToBluetoothAdapter:
    def __init__(self, adapter: OldMusicPlayer):
        self.adapter = adapter

    def play_bluetooth(self):
        return self.adapter.play_jack()
        


old_player = OldMusicPlayer()
adapter = JackToBluetoothAdapter(old_player)
print(adapter.play_bluetooth())  # "Playing music via 3.5mm Jack"
