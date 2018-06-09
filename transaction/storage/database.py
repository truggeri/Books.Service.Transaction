""" Data store module
    Acts as a layer between service and implementation of a database
"""

from cloudant.client import CouchDB

class Database:
    client: CouchDB
    
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
    
    def connect(self) -> None:
        self.client = CouchDB(
            user=self.username,
            auth_token=self.password,
            url="http://127.0.0.1:5984")

    def create(self):
        print(">> create")

    def read(self):
        print(">> read")

    def update(self):
        print(">> update")

    def delete(self):
        print(">> delete")

    def disconnect(self) -> None:
        self.client.disconnect()
    