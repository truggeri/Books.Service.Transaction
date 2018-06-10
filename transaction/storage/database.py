""" Data store module
    Acts as a layer between service and implementation of a database
"""

from cloudant.client import CouchDB
from typing import Tuple

from transaction.config import cfg

_client: CouchDB
    
def connect() -> None:
    _client = CouchDB(
        user=cfg["DB_USERNAME"],
        auth_token=cfg["DB_PASSWORD"],
        url=cfg["DB_HOST_URL"],
        connect=True)

def health() -> Tuple[bool, dict]:
    result = _client.session()
    if "ok" not in result:
        return (False, {})
    return (True, result)

def disconnect() -> None:
    _client.disconnect()
    