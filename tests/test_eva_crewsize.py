import pytest
from eva_data_analysis import calculate_crew_size

@pytest.mark.parametrize("input_value, expected_result", [
    ("Louis Armstrong;", 1),
    ("Louis Armstrong; Bugs Bunny;", 2)
])
def test_calculate_crew_size(input_value, expected_result):
    """
    Test that it returns ground truth values for typical crew values
    """
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result

def test_crew_size_edge():
    # missing string element
    assert calculate_crew_size(("")) == None