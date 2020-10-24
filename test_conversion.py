import pytest
from main import convert_to_float

def test_standard():
	assert convert_to_float("$3 million") == 3000000

def test_standard_double_digit():
	assert convert_to_float("$99 million") == 99000000

def test_standard_with_decimal():
	assert convert_to_float("$3.5 million") == 3500000

def test_standard_multiple_decimals():
	assert convert_to_float("$1.234 million") == 1234000

def test_standard_billion():
	assert convert_to_float("$1.25 billion") == 1250000000

def test_standard_thousand():
	assert convert_to_float("$900.9 thousand") == 900900

def test_range():
	assert convert_to_float("$3.5-4 million") == 3500000

def test_range_with_to():
	assert convert_to_float("$3.5 to 4 million") == 3500000

def test_number():
	assert convert_to_float("$950000") == 950000

def test_number_with_commas():
	assert convert_to_float("$127,850,000") == 127850000

def test_number_with_commas_and_decimals():
	assert convert_to_float("$10,000,000.50") == 10000000

def test_number_with_commas_middle():
	assert convert_to_float("estimated $5,000,000 (USD)") == 5000000

def test_other_currency():
	assert convert_to_float("60 million Norwegian Kroner (around $8.7 million in 1989)") == 8700000

def test_list():
	assert convert_to_float(['$410.6 million (gross)', '$378.5 million (net)']) == 410600000

def test_unkown():
	assert convert_to_float("70 crore") is None