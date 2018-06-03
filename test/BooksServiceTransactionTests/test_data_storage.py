import pytest
    
@pytest.fixture
def data_storage():
    from BooksServiceTransaction.Data.Storage import DataStorage
    return DataStorage()

def test_health_whenok_thentrue(data_storage):
    result = data_storage.Health()
    assert result == True