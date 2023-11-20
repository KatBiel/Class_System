from lib.todo import *

def test_initialise_todo():
    todo = Todo('Walk the dog')
    assert todo.task == 'Walk the dog'
    assert todo.complete == False

def test_mark_task_as_complete():
    todo = Todo('Walk the dog')
    todo.mark_complete()
    assert todo.complete == True