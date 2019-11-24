from datetime import datetime
from decimal import Decimal


def date_factory(s):
    return datetime.strptime(s, '%d%m%Y').date()


def monetary_factory(s):
    return Decimal(s) / 100


def hour_factory(s):
    return datetime.strptime(s, '%H%M%S').time()


def month_year_factory(s):
    return datetime.strptime(s, '%m%Y').date()


def card_number_factory(s):
    return str(s)