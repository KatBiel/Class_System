from lib.todo import *
from lib.todo_list import *

def test_add_single_todo():
    todolist = TodoList()
    task_1 = Todo('Walk the dog')
    todolist.add(task_1)
    assert todolist.incomplete() == [task_1]

def test_add_multiple_uncompleted_todos():
    todolist = TodoList()
    task_1 = Todo('Walk the dog')
    task_2 = Todo('Feed the cats')
    task_3 = Todo('Wash the dishes')
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.add(task_3)
    assert todolist.incomplete() == [task_1, task_2, task_3]

def test_add_multiple_todos():
    todolist = TodoList()
    task_1 = Todo('Walk the dog')
    task_2 = Todo('Feed the cats')
    task_3 = Todo('Wash the dishes')
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.add(task_3)
    task_2.mark_complete()
    assert todolist.incomplete() == [task_1, task_3]
    assert todolist.complete() == [task_2]

def test_give_up():
    todolist = TodoList()
    task_1 = Todo('Walk the dog')
    task_2 = Todo('Feed the cats')
    task_3 = Todo('Wash the dishes')
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.add(task_3)
    todolist.give_up() 
    assert todolist.incomplete() == []
    assert todolist.complete() == [task_1, task_2, task_3]