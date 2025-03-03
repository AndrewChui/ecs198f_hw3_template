import pytest
from foo_bar_baz import foo_bar_baz

# Add testcases Here

def test_easy_cases():
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(2) == "1 2"

def test_multiple_of_three():
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(6) == "1 2 Foo 4 Bar Foo"
    assert foo_bar_baz(9) == "1 2 Foo 4 Bar Foo 7 8 Foo"

def test_multiple_of_five():
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"
    assert foo_bar_baz(10) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar"
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

def test_multiple_of_three_and_five():
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"
    assert foo_bar_baz(30) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz"

def test_edge_cases():
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(1) == "1" 

