""" Data store module
    Acts as a layer between service and implementation of a database
"""

from cloudant.client import CouchDB
from typing import Tuple

from transaction.config import cfg

class Database:
    client: CouchDB
    
    def __init__(self) -> None:
        pass
    
    def connect(self) -> None:
        self.client = CouchDB(
            user=cfg["DB_USERNAME"],
            auth_token=cfg["DB_PASSWORD"],
            url=cfg["DB_HOST_URL"],
            connect=True)

    def health(self) -> Tuple[bool, dict]:
        result = self.client.session()
        if "ok" not in result:
            return (False, {})
        return (True, result)
    
    def disconnect(self) -> None:
        self.client.disconnect()

    def create(self):
        print(">> create")

    def read(self):
        print(">> read")

    def update(self):
        print(">> update")

    def delete(self):
        print(">> delete")
    