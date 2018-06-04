import pytest
    
@pytest.fixture
def health_controller():
    from BooksServiceTransaction.controllers import HealthController
    return HealthController()

def test_health_whenok_then200(health_controller):
    (resultStr, resultInt) = health_controller.ok()
    assert resultInt == 200
    