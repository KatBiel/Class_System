from lib.todo_list import *

def test_initially_has_no_todos():
    list = TodoList()
    assert list.tasks == []

def test_empty_incomplete():
    list = TodoList()
    assert list.incomplete() == []