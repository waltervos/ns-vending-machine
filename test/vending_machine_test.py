from hamcrest import assert_that, equal_to
from vending_machine import VendingMachine, Choice, Can
import pytest


class TestVendingMachine:
  
  @pytest.fixture()
  def vending_machine(self):
    vending_machine = VendingMachine()
    vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA) 
    vending_machine.configure(Choice.COKE, Can.COLA) 
    return vending_machine

  def test_given_a_vending_machine_when_unconfigured_then_does_not_deliver_can_of_choice(self, vending_machine):
    assert_that(vending_machine.deliver(Choice.BEER), equal_to(Can.NOTHING))

  def test_vending_machine_delivers_can_of_cola_for_coke_choice(self, vending_machine):
    assert_that(vending_machine.deliver(Choice.COKE), equal_to(Can.COLA))
    
  def test_vending_machine_delivers_can_of_fanta_for_fizzy_orange_choice(self, vending_machine):
    assert_that(vending_machine.deliver(Choice.FIZZY_ORANGE), equal_to(Can.FANTA))
    