def create(table_name, columns):
    DB = database(table_name, columns)
    print ('TABLE', table_name, 'HAS BEEN CREATED')
    return DB

class database:
    def __init__(self, table_name, columns) -> None:
        self.table_name = table_name
        self.tables = {}

    def select(self, table_name):
        print ('SELECTED', table_name)
    
    def insert(self, table_name, values):
        print ('INSERTED ROW WITH ', values, ' IN ', table_name)

    def delete(self, table_name):
        print ('DELETED', table_name)