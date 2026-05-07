from eva_data_analysis import text_to_duration

def test_text_to_duration_float():
    assert abs(text_to_duration("10:20") - 10.333) < 1e5

def test_text_to_duration_integer():
    input_value = "10:00"
    assert text_to_duration(input_value) == 10

test_text_to_duration_float()
test_text_to_duration_integer()