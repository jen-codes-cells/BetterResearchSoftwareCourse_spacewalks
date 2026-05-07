import pytest
from eva_data_analysis import calculate_crew_size

def test_eva_crewsize():
    """
    To test the calculate_crew_size function
    """
    # Single crew member
    assert calculate_crew_size(("Louis Armstrong;")) == 1

    # Two members
    assert calculate_crew_size(("Louis Armstrong; Bugs Bunny;")) == 2

def test_eva_crew_size_edge():
    # missing string element
    assert calculate_crew_size(("")) == None