""" Test cases for the transaction.storage.database module
"""

from unittest.mock import ANY, MagicMock, patch

from cloudant.client import CouchDB
import pytest

from context import transaction

mocked_couch = MagicMock(spec=CouchDB)
    
@pytest.fixture
def transaction_db():
    fixture = transaction.storage.database.Database("fakeuser", "fakepass")
    fixture.client = mocked_couch
    return fixture

@patch("transaction.storage.database.CouchDB")
def test_database_whenconnect_thenconnectcalled(mock_couch, transaction_db):
    transaction_db.connect()
    mock_couch.assert_called_with(user="fakeuser", auth_token="fakepass", url=ANY)

def test_database_whendisconnect_thendisconnectcalled(transaction_db):
    transaction_db.disconnect()

    assert mocked_couch.disconnect.called
