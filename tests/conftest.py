import pytest

@pytest.fixture
def sample_employees():
    return [
        {"name": "Alice", "hours_worked": 160, "rate": 50, "department": "Marketing"},
        {"name": "Bob", "hours_worked": 150, "rate": 40, "department": "Design"},
        {"name": "Carol", "hours_worked": 170, "rate": 60, "department": "Design"},
    ]
