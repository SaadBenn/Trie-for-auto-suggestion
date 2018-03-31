import node

class Trie:

    def __init__(self):
        self.root = node('*')

    def add(self, word):
        """
        Add the word to Trie data structure
        """
        root_node = self.root

        for letter in word:
            found_in_child = False

            for child in root_node.get_children():
                # compare letters
                if child.get_char() == letter:
                    # We found it, increase the counter by 1 to keep track that another
                    # word has it as well
                    root_node.increment_count()
                    # And point the node to the child that contains this char
                    root_node = child
                    found_in_child = True
                    break

            # We did not find it so add a new child
            if not found_in_child:
                new_node = node(letter)
                root_node.get_children().append(new_node)
                # And then point node to the new child
                root_node = new_node

        # Everything finished. Mark it as the end of a word.
        node.word_finished = True

    def find_prefix(self, prefix):
        """
        Check and return
        1. If the prefix exists in any of the words we added so far
        2. If yes then how may words actually have the prefix
        """
        node = self.root

        if not node.get_children():
            return False, 0

        for letter in prefix:
            char_not_found = True

            # Search through all the children of the present `node`
            for child in node.get_children():
                if child.get_char() == letter:
                    # We found the char existing in the child.
                    char_not_found = False
                    # Assign node as the child containing the char and break
                    node = child
                    break

            # Return False anyway when we did not find a char.
            if char_not_found:
                return False, 0
        # Well, we are here means we have found the prefix. Return true to indicate that
        # And also the counter of the last node. This indicates how many words have this
        # prefix
        return True, node.get_count()
