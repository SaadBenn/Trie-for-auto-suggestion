from Trie import Trie


def main():
    # Create a new Trie structure
    trie = Trie()
    # Add some words for testing
    trie.add('hackathon')
    trie.add('hack')

    # Check for the number of times we have prefixes
    print(trie.find_prefix('hac'))
    print(trie.find_prefix('hack'))
    print(trie.find_prefix('hackathon'))
    print(trie.find_prefix('ha'))
    print(trie.find_prefix('hammer'))


if __name__ == '__main__':
    main()
