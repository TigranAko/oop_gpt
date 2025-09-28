#OldCharger должен иметь метод charge_micro_usb(), который выводит: .

#NewSmartphone должен иметь метод charge_usb_c(), который выводит: "Charging via USB-C".

#Адаптер MicroUSBtoUSBCAdapter должен преобразовывать charge_usb_c() в charge_micro_usb().


class OldCharger:
    def charge_micro_usb(self):
        print("Charging via MicroUSB")


#class NewCharger:
#    def charge_usb_c(self):
#        print("Charging via USB-C")

#class MicroUSBtoUSBCAdapter(NewCharger):
class MicroUSBtoUSBCAdapter:
    def __init__(self, adapter):
        self.adapter = adapter

    def charge_usb_c(self):
        self.adapter.charge_micro_usb()

old_charger = OldCharger()
adapter = MicroUSBtoUSBCAdapter(old_charger)

adapter.charge_usb_c()  # "Charging via MicroUSB"
