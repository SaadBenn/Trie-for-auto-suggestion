class Node:
    """
    Trie node implementation.
    """

    def __init__(self, key):
        self._char = key
        self._children = []
        # Is it the last character of the word.`
        self._is_word_finished = False
        # How many times this character appeared in the addition process
        self._count = 1

# Getters for the instance private variables, maintaining integrity + following encapsulation
    @property
    def get_char(self):
        return self._char

    @property
    def get_children(self):
        return self._children

    @property
    def get_word_finished(self):
        return self._is_word_finished

    @property
    def increment_count(self):
        self._count += 1

    @property
    def get_count(self):
        return self._count
