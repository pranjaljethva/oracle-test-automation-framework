import pytest
from pytest_bdd import given, when, then, step


def test_login(page):
    page.goto("https://myapp.com/login")
    
