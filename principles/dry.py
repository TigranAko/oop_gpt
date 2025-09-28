#bad
class Database:
    def connect_mysql(self):
        print("Connecting to MySQL")

    def connect_postgres(self):
        print("Connecting to PostgreSQL")

# my соответствует принципу dry
# my + solid

class Database:
    def connect(self, sql):
        print("Connecting to {sql}")


from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL")

class PostgreSQLDatabase(Database)
    def connect(self):
        print("Connecting to PostgreSQL")
