import json
import urllib
from pytest import raises, fixture
from src.read_write_customers import get_customers

@fixture
def customers():
    customersList = get_customers("https://s3.amazonaws.com/intercom-take-home-test/customers.txt")
    yield customersList

def test_valid_customers_url(customers):
    assert len(customers) == 32
    assert customers[1]["name"] == "Alice Cahill"
    for customer in customers:
        assert len(customer) == 4
        assert 'user_id' in customer
        assert 'name' in customer
        assert 'latitude' in customer
        assert 'longitude' in customer

# Test for not an input file
def test_invalid_inputFile_url():
    with raises(json.JSONDecodeError):
        get_customers("https://www.dublin.ie")

# Test for invalid URL
def test_invalid_url():
    with raises(urllib.error.URLError):
        get_customers("http://urlNotFount.com/")

# Tests for checking validity of data in each customer data
def test_customer_name(customers):
    for customer in customers:
        if 'name' not in customer:
            assert False
    assert True

def test_customer_user_id(customers):
    for customer in customers:
        if 'user_id' not in customer:
            assert False
    assert True

def test_customer_latitude(customers):
    for customer in customers:
        if 'latitude' not in customer:
            assert False
    assert True

def test_customer_longitude(customers):
    for customer in customers:
        if 'longitude' not in customer:
            assert False
    assert True
