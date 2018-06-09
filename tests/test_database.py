import pytest
from pytest_mock import mocker
from unittest.mock import patch

from context import transaction
    
@pytest.fixture
def transaction_db():
    return transaction.storage.database.Database("fakeuser", "fakepass")

@patch('transaction.storage.database.CouchDB')
def test_database_whenconnect_thenconnectcalled(mock_couch, transaction_db):
    transaction_db.connect()
    mock_couch.assert_called_with(user="fakeuser", auth_token="fakepass", url="http://127.0.0.1:5984")
    