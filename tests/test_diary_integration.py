from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_a_multiple_entries():
    diary = Diary()
    entry_1 = DiaryEntry('My title', 'My contents')
    entry_2 = DiaryEntry('My title 2', 'My contents 2')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

def test_count_words_in_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry('My title', 'My contents')
    entry_2 = DiaryEntry('My title 2', 'My contents 2')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5

def test_reading_time():
    diary = Diary()
    entry_1 = DiaryEntry('My title', 'My contents')
    entry_2 = DiaryEntry('My title 2', 'My contents 2')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 2

def test_find_entry_for_reading_time():
    diary = Diary()
    entry_1 = DiaryEntry('My title', 'My contents')
    entry_2 = DiaryEntry('My title 2', 'My contents one two three')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_2

'''
return None if dont have time to read any entry
'''

def test_find_entry_for_reading_time_less_than_entry():
    diary = Diary()
    entry_1 = DiaryEntry('My title', 'My contents one two three')
    entry_2 = DiaryEntry('My title 2', 'four five six')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 1) == None

