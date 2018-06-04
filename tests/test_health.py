import pytest

from context import transaction
    
@pytest.fixture
def health_controller():
    return transaction.controllers.health.HealthController()

def test_health_whenok_then200(health_controller):
    (__, resultInt) = health_controller.ok()
    assert resultInt == 200

def test_health_whenhealth_then200(health_controller):
    (resultJson, resultInt) = health_controller.health()
    assert resultInt == 200
    exp_string = '{\n    "Healthy": true\n}'
    assert exp_string == resultJson
    