import pytest
from biscuits import parse


@pytest.mark.parametrize('input,expected', [
    ('', {}),
    ('key=value', {'key': 'value'}),
    ('key=123', {'key': '123'}),
    ('key=печенье', {'key': 'печенье'}),
    ('key=value; other=value2', {'key': 'value', 'other': 'value2'}),
    ('FOO    =bar; baz  =raz', {'FOO': 'bar', 'baz': 'raz'}),
    ('FOO= bar; baz=   raz', {'FOO': 'bar', 'baz': 'raz'}),
    ('FOO=bar   ; baz=raz  ', {'FOO': 'bar', 'baz': 'raz'}),
    ("  f   ;   FOO  =   bar;  ; f ; baz = raz", {'FOO': 'bar', 'baz': 'raz'}),
    ('FOO    =   "bar"   ; baz ="raz"  ', {'FOO': 'bar', 'baz': 'raz'}),
    ('foo="bar=123&name=Magic+Mouse"', {'foo': 'bar=123&name=Magic+Mouse'}),
    ('foo=bar=baz', {'foo': 'bar=baz'}),
    ('a=Zm9vIGJhcg==', {'a': 'Zm9vIGJhcg=='}),
    ('foo=%20%22%2c%3b%2f', {'foo': ' ",;/'}),
    ('foo=%xx', {}),  # Invalid hex code.
    ('foo=%x', {}),  # Invalid hex code.
    ('foo="?foo', {'foo': '?foo'}),
    ("x=!#$&'()*+-./01", {'x': "!#$&'()*+-./01"}),
])
def test_parse(input, expected):
    assert parse(input) == expected
