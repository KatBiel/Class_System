class DiaryEntry:
    def __init__(self, title, contents): 
        self.title = title
        self.contents = contents
        self.stop_off_point = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return wpm * 10

    def reading_chunk(self, wpm, minutes):
        readable_number_of_words = wpm * minutes
        words = self.contents.split()
        start_point = self.stop_off_point
        end_point = self.stop_off_point + readable_number_of_words
        read_already = ' '.join(words[start_point:end_point])
        self.stop_off_point += readable_number_of_words
        return read_already
        