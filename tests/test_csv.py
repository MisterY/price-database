""" Test CSV parsing """
from datetime import datetime
from decimal import Decimal
from pricedb.csv import CsvParser


def test_loading_file(csv_path):
    """ load csv file """
    parser = CsvParser()
    actual = parser.parse_file(csv_path, "EUR")

    assert actual


def test_types(csv_path):
    """ Test correct parsing """
    parser = CsvParser()
    prices = parser.parse_file(csv_path, "EUR")
    for price in prices:
        assert isinstance(price.datetime, datetime)
        assert isinstance(price.value, Decimal)
        assert isinstance(price.symbol, str)


def test_symbol_translation(session):
    """ test translating symbols """
    parser = CsvParser()
    actual = parser.translate_symbol("AEF.AX")

    assert actual == "ASX:AEF"
