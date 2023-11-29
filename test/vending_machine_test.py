import pytest
from hamcrest import assert_that, equal_to
from vending_machine import Can, Choice, VendingMachine


class TestFreeDrinksVendingMachine:

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


class TestPaidDrinksVendingMachine:

    @pytest.fixture()
    def vending_machine(self):
        vending_machine = VendingMachine()
        vending_machine.configure(Choice.FIZZY_ORANGE, Can.FANTA, 400)
        vending_machine.configure(Choice.COKE, Can.COLA, 500)
        return vending_machine

    def test_vending_machine_delivers_no_can_of_cola_for_unpaid_coke_choice(self, vending_machine):
        assert_that(vending_machine.deliver(Choice.COKE), equal_to(Can.NOTHING))

    def test_vending_machine_delivers_can_of_cola_for_paid_coke_choice(self, vending_machine):
        vending_machine.insert(500)
        assert_that(vending_machine.deliver(Choice.COKE), equal_to(Can.COLA))

    def test_vending_machine_delivers_can_of_cola_for_too_much_paid_coke_choice(self, vending_machine):
        vending_machine.insert(600)
        assert_that(vending_machine.deliver(Choice.COKE), equal_to(Can.COLA))

    def test_vending_machine_delivers_can_of_fanta_for_paid_fizzy_orange_choice(self, vending_machine):
        vending_machine.insert(400)
        assert_that(vending_machine.deliver(Choice.FIZZY_ORANGE), equal_to(Can.FANTA))

    def test_vending_machine_delivers_nothing_for_second_paid_coke_choice(self, vending_machine):
        vending_machine.insert(500)
        _ = vending_machine.deliver(Choice.COKE)
        assert_that(vending_machine.deliver(Choice.COKE), equal_to(Can.NOTHING))
