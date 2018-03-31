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

