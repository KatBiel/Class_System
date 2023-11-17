from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_a_multiple_entries():
    diary = Diary()
    entry_1 = DiaryEntry('My title', 'My contects')
    entry_2 = DiaryEntry('My title 2', 'My contects 2')
    diary.add('entry_1')
    diary.add('entry_2')
    assert diary.all == [entry_1, entry_2]