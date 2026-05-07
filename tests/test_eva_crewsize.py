import pytest
from eva_data_analysis import calculate_crew_size

def test_eva_crewsize():
    """
    To test the calculate_crew_size function
    """
    # Single crew member
    assert calculate_crew_size(("Louis Armstrong;")) == 1

    # missing string element
    assert calculate_crew_size(("Bugs Bunny")) == 1

    # incorrect string format
    assert calculate_crew_size(("Bugs Bunny;;")) == 1