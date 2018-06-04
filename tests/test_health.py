import pytest

from context import transaction
    
@pytest.fixture
def health_controller():
    return transaction.controllers.health.HealthController()

def test_health_whenok_then200(health_controller):
    (resultStr, resultInt) = health_controller.ok()
    assert resultInt == 200
    