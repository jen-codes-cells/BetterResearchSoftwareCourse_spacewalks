import pytest
from eva_data_analysis import text_to_duration

def test_text_to_duration_float():
    """
    Test that text_to_duration returns expected ground truth values 
    with a non zero minute component.
    """
    assert text_to_duration("10:20") ==  pytest.approx(10.3333333)

def test_text_to_duration_integer():
    """
    Test that text_to_duration returns expected ground truth values 
    for typical whole hour durations.
    """
    input_value = "10:00"
    assert text_to_duration(input_value) == 10
