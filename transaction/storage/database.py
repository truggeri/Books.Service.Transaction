class DataStore():

    def __init__(self, connection_string):
        self._conn_str = connection_string

    def create(self):
        print(">> create")

    def read(self):
        print(">> read")

    def update(self):
        print(">> update")

    def delete(self):
        print(">> delete")
    
