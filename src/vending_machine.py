from dataclasses import dataclass
from enum import Enum
from typing import Any


class Button(Enum):
    COLA = "Cola choice"
    FIZZY_ORANGE = "Fizzy orange choice"
    BEER = "Beer choice"


class Can(Enum):
    NOTHING = "No can"
    COKE = "Can of Coke"
    FANTA = "Can of Fanta"


@dataclass
class Drawer:
    can_type: Can
    price_in_cents: int
    vending_machine: "VendingMachine" = None

    def _pay_for_can(self):
        self.vending_machine._balance_in_cents -= self.price_in_cents

    def _can_afford_can(self):
        return self.price_in_cents <= self.vending_machine._balance_in_cents
    
    def drop_can(self):
        if self._can_afford_can():
            self._pay_for_can()
            return self.can_type
        return Can.NOTHING
        

class VendingMachine:
    def __init__(self):
        self._choice_can_map: dict[Button, Drawer] = {}
        self._balance_in_cents = 0
        
    def deliver(self, choice):
        if self._available(choice):
            drawer = self._choice_can_map[choice]
            return drawer.drop_can()
        return Can.NOTHING

    def insert(self, amount_in_cents):
        self._balance_in_cents = amount_in_cents

    def configure(self, choice, can_type, price_in_cents=0):
        self._choice_can_map[choice] = Drawer(can_type, price_in_cents, self)

    def _available(self, choice):
        return choice in self._choice_can_map
    
    
    
    