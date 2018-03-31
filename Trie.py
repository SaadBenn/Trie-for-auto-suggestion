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
                if child.char == letter:
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
