""" Test cases for the transaction.storage.database module
"""

from unittest.mock import ANY, MagicMock, patch

from cloudant.client import CouchDB
import pytest

from context import transaction
    
@pytest.fixture
def transaction_db():
    return transaction.storage.database.Database("fakeuser", "fakepass")

@patch("transaction.storage.database.CouchDB")
def test_database_whenconnect_thenconnectcalled(mock_couch, transaction_db):
    transaction_db.connect()
    mock_couch.assert_called_with(user="fakeuser", auth_token="fakepass", url=ANY)

def test_database_whendisconnect_thendisconnectcalled(transaction_db):
    mocked_couch = MagicMock(spec=CouchDB)
    transaction_db.client = mocked_couch

    transaction_db.disconnect()

    assert mocked_couch.disconnect.called
    
