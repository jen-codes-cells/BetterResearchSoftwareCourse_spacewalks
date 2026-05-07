from eva_data_analysis import text_to_duration

def test_text_to_duration_float();
    assert text_to_duration("10:15") == 10.25

def test_text_to_duration_integer():
    input_value = "10:00"
    assert text_to_duration(input_value) == 10

test_text_to_duration_float()
test_text_to_duration_integer()