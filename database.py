from abc import ABC, abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self, data, id):
        pass

    @abstractmethod
    def update(self, data, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass

class SQLDatabase(IDatabaseOperations):
    def __init__(self):
        self.info = []  

    def insert(self, data, id):
        self.info.append({"data": data, "id": id})

    def update(self, data, id):
        for x in self.info:
            if x["id"] == id:
                x["data"] = data 

    def delete(self, id):
        self.info = [x for x in self.info if x["id"] != id]  

    def display(self):
        print("SQL Database:", self.info)

class NoSQLDatabase(IDatabaseOperations):
    def __init__(self):
        self.info = {}  

    def insert(self, data, id):
        self.info[id] = data  

    def update(self, data, id):
        if id in self.info:
            self.info[id] = data  

    def delete(self, id):
        if id in self.info:
            del self.info[id]  
    def display(self):
        print("NoSQL Database:", self.info)


sql_db = SQLDatabase()
nosql_db = NoSQLDatabase()


sql_db.insert("A", 1)
sql_db.insert("B", 2)
sql_db.display()

sql_db.update("updated a", 1)
sql_db.display()

sql_db.delete(2)
sql_db.display()


nosql_db.insert("A1", 1)
nosql_db.insert("B1", 2)
nosql_db.display()

nosql_db.update("updated A1", 1)
nosql_db.display()

nosql_db.delete(2)
nosql_db.display()
