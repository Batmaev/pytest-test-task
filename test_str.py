import pytest

def test_string_format():
    var = 3
    assert f'var is {var}' == 'var is 3'

@pytest.mark.parametrize('input, output', [
    ('aa', 'AA'),
    ('AA', 'AA'),
    ('ы' , 'Ы' ),
    ('aßc', 'ASSC'),
    ('$#^1\n\t\r', '$#^1\n\t\r')
])
def test_upper(input, output):
    assert input.upper() == output

# Негативный тест
def test_find():
    line = 'kill me, please'
    substr = 'please!'
    assert line.find(substr) == -1