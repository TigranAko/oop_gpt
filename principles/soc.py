class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        return f"Report data: {self.data}"

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.generate_report())

    def send_email(self):
        print("Sending report via email...")



class Report:
    def __init__(self, data, send_type=EmailSender):
        self.data = data
        self.send_type = send_type

    def generate_report(self):
        return f"Report data: {self.data}"

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.generate_report())

    def send(self):
        self.send_type.send()

class EmailSender:
    def send(self):
        print("Sending report via email...")



class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Report data: {self.data}"

class FileSaver:
    @staticmethod
    def save(report: Report, filename):
        with open(filename, "w") as file:
            file.write(report.generate())

class EmailSender:
    @staticmethod
    def send(report: Report):
        print(f"Sending report via email...\n{report.generate()}")

# Используем классы
report = Report("Sales data")

# Сохранение в файл
FileSaver.save(report, "report.txt")

# Отправка по email
EmailSender.send(report)

