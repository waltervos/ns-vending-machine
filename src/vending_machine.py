from enum import Enum


class Choice(Enum):
    COKE = "Coke choice"
    FIZZY_ORANGE = "Fizzy orange choice"
    BEER = "Beer choice"


class Can(Enum):
    NOTHING = "no can"
    COLA = "Can of Cola"
    FANTA = "Can of Fanta"


class VendingMachine:
    def __init__(self):
        self._choice_can_map = {}
        self._choice_price_map = {}
        self._balance_in_cents = 0

    def deliver(self, choice):
        if not choice in self._choice_can_map:
            return Can.NOTHING

        price_in_cents = self._choice_price_map[choice]
        if price_in_cents > self._balance_in_cents:
            return Can.NOTHING

        self._balance_in_cents -= price_in_cents
        return self._choice_can_map[choice]

    def insert(self, amount_in_cents):
        self._balance_in_cents = amount_in_cents

    def configure(self, choice, can, price_in_cents=0):
        self._choice_can_map[choice] = can
        self._choice_price_map[choice] = price_in_cents
