""" Data store module
    Acts as a layer between service and implementation of a database
"""

from cloudant.client import CouchDB

from transaction.config import cfg

class Database:
    client: CouchDB
    
    def __init__(self) -> None:
        pass
    
    def connect(self) -> None:
        self.client = CouchDB(
            url=cfg["DB_HOST_URL"],
            user=cfg["DB_USERNAME"],
            auth_token=cfg["DB_PASSWORD"])

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
    