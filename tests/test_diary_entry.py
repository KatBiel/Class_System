from lib.diary_entry import DiaryEntry

def test_construct_entry():
    entry = DiaryEntry('My title', 'My entry')
    assert entry.title == 'My title'
    assert entry.contents == 'My entry'

def test_count_words():
    entry = DiaryEntry('My title', 'My contents')
    assert entry.count_words() == 2

def test_reading_time():
    entry = DiaryEntry('My title', 'My contents')
    assert entry.reading_time(2) == 20

def test_reading_chunk():
    entry = DiaryEntry('My title', 'My contents: one two three four five')
    assert entry.reading_chunk(2, 1) == 'My contents:'

# If called again, `reading_chunk` should return the next chunk,
# skipping what has already been read, until the contents is fully read.
# The next call after that it should restart from the beginning.

def test_reading_second_chunk():
    entry = DiaryEntry('My title', 'My contents: one two three four five')
    assert entry.reading_chunk(2, 1) == 'My contents:'
    assert entry.reading_chunk(2, 1) == 'one two'