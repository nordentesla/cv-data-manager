import pytest
from main import input_data_manager

def test_input_data_manager():
    assert input_data_manager("hello", "Enter hello: ", str, "")