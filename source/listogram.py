#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        word = str(word)
        found = False
        self.tokens += count
        # OLD WAY
        # import pdb; pdb.set_trace()
        # if len(self) == 1:
        #     if self[0][0] == word:
        #         self[0][1] += count
        #         found = True
        # elif len(self) > 1:
        #     for i in range(0, len(self) - 1):
        #         if self[i][0] == word:
        #             self[i][1] += count
        #             found = True
        #             break
        # if found == False:
        #     self.types += 1
        #     self.append([word, count])
        # print("This is the length: " + str(len(self)))
        # for i in range(0, len(self)):
        #     print("This num: " + str(i))
        for i in range(0, len(self)):
            if self[i][0] == word:
                self[i][1] += count
                found = True
                break
        if found == False:
            self.types += 1
            self.append([word, count])

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        # Dont want to duplicate code
        # freq = 0
        # if len(self) == 1:
        #     if self[0][0] == word:
        #         freq = self[0][1]
        # elif len(self) > 1:
        #     for i in range(0, len(self) - 1):
        #         if self[i][0] == word:
        #             freq = self[i][1]
        #             break
        word = str(word)
        index = self._index(word)
        return self[index][1] if index != None else 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        # Dont want to duplicate code
        # found = False
        # if len(self) == 1:
        #     if self[0][0] == word:
        #         found = True
        # elif len(self) > 1:
        #     for i in range(0, len(self) - 1):
        #         if self[i][0] == word:
        #             found = True
        #             break
        word = str(word)
        index = self._index(word)
        return True if index != None else False

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        target = str(target)
        index = None
        # OLD WAY
        # if len(self) == 1:
        #     if self[0][0] == target:
        #         index = 0
        # elif len(self) > 1:
        #     for i in range(0, len(self) - 1):
        #         if self[i][0] == target:
        #             index = i
        #             break
        for i in range(0, len(self)):
            if self[i][0] == target:
                index = i
                break
        return index


def print_histogram(word_list):
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
