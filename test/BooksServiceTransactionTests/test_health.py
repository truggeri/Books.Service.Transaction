import pytest
    
@pytest.fixture
def health_controller():
    from BooksServiceTransaction.Controllers import HealthController
    return HealthController()

def test_health_whenok_then200(health_controller):
    (resultStr, resultInt) = health_controller.Ok()
    assert resultInt == 200
    