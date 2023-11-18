from lib.diary import *

def test_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []

