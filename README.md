# Trie

Trie Data structure is used under the hood in almost every computer including smart phones. The keyboard that you get on your phone uses the same data structure, when you start typing a word and it starts showing you suggestions. This is the idea behind Trie data structure. Tries are also used for matching algorithms and implementing things like spellcheckers. Another good example is Google's ```Did you mean....?```

# Why Trie
Tries are very useful for certain situations. Here are some of the advantages:

* Looking up values typically have a better worst-case time complexity.
* Unlike a hash map, a Trie does not need to worry about key collisions.
* Doesn't utilize hashing to guarantee a unique path to elements.
* Trie structures can be alphabetically ordered by default.

Read up more on [Trie](https://en.wikipedia.org/wiki/Trie) data structure.

The goal of this project is to mimic the implementation of auto suggestion feature of keyboards using Trie data structure in Python. 

# Note
It’s worth mentioning that search engines probably have more complexity to their tries, since they will return certain terms based on how popular they are, and likely have some additional logic to determine the weight associated with certain terms in their trie structures. But, under the hood, they probably are using tries to make this magic happen!
