# -*- coding: utf-8 -*-
from decimal import Decimal


class Fees(object):
    """"""
    def __init__(self):
        """
        конструктор
        """
        self._fee = None

    @property
    def fee(self):
        """
        возвращаем текущую комиссию
        """
        return self._fee

    @fee.setter
    def fee(self, value):
        """
        устанавливаем размер комиссии
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value


f = Fees()
f.fee = "1"

print(f.fee)
