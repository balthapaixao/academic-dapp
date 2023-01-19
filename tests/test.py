import pytest
from brownie import accounts


@pytest.fixture(scope="module")
def token(Token):
    yield Token.deploy("Test Token", "TST", 18, 1e20, {'from': accounts[0]})


def test_transferFrom(fn_isolation, token):
    token.approve(accounts[1], 6e18, {'from': accounts[0]})
    token.transferFrom(accounts[0], accounts[2], 5e18, {'from': accounts[1]})

    assert token.balanceOf(accounts[2]) == 5e18
    assert token.balanceOf(accounts[0]) == 9.5e19
    assert token.allowance(accounts[0], accounts[1]) == 1e18


def test_balance_allowance(fn_isolation, token):
    assert token.balanceOf(accounts[0]) == 1e20
    assert token.allowance(accounts[0], accounts[1]) == 0