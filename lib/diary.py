import math

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries

    def count_words(self):
        word_count = [entry.count_words() for entry in self.entries]
        return sum(word_count)

    def reading_time(self, wpm):
        return math.floor(self.count_words() / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        length_of_readable_string = wpm * minutes
        readable_entries = []
        for entry in self.entries:
            if entry.count_words() <= length_of_readable_string:
                    readable_entries.append(entry)
        if readable_entries == []:
            return None
        organised_entries = sorted(readable_entries, key=lambda x: x.count_words(), reverse=True)
        return organised_entries[0]

        # length_of_readable_string = wpm * minutes
        # most_readable = None
        # longest_found_so_far = 0 
        # for entry in self.entries:
        #     if entry.count_words() <= length_of_readable_string:
        #         if entry.count_words() > longest_found_so_far:
        #             most_readable = entry
        #             longest_found_so_far = entry.count_words()
        # return most_readable
# Returns:
#   An instance of DiaryEntry representing the entry that is closest to,
#   but not over, the length that the user could read in the minutes
#   they have available given their reading speed.
