
def test_value(value):
    if value < 100:
    	return 'The value is just right'
    else:
    	return 'The value is too big!'


def test_value_1(value):
    return 'The value is ' + ('just right.' if value < 100 else 'too big!')

def test_value_2(value):
    return 'The value is ' + (value < 100 and 'just right' or 'too big!')

