from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    input_value = "10:00"
    test_result = text_to_duration(input_value) == 10.0
    print(f"text_to_duration('10:00') result == 10.0? {test_result}")

test_text_to_duration_integer()