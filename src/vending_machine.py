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
    
  def deliver(self, choice):
    return self._choice_can_map[choice] if choice in self._choice_can_map else Can.NOTHING
  
  def configure(self, choice, can):
    self._choice_can_map[choice] = can
