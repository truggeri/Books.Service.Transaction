""" Test cases for the transaction.storage.database module
"""

from unittest.mock import ANY, MagicMock, patch

from cloudant.client import CouchDB
import pytest

from context import transaction
from transaction.config import cfg

mocked_couch = MagicMock(spec=CouchDB)
    
@pytest.fixture
def transaction_db():
    cfg["DB_USERNAME"] = "fakeuser"
    cfg["DB_PASSWORD"] = "fakepass"
    fixture = transaction.storage.database
    fixture.__client = mocked_couch
    return fixture

@patch("transaction.storage.database.CouchDB")
def test_database_whenconnect_thenconnectcalled(patch_couch, transaction_db):
    transaction_db.connect()

    assert patch_couch.call_args == ({"user": "fakeuser", "auth_token": "fakepass", "url": ANY, "connect": True}, )

def test_database_whendisconnect_thendisconnectcalled(transaction_db):
    transaction_db.disconnect()

    assert mocked_couch.disconnect.called
