from trie_node import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # get the index of a specific character
    # returns the Unicode code for a character
    # used to convert a single Unicode character to its integer equivalent
    # remember that it goes from lowest unicode value for letters -> a
    # so this takes the order of the single character inputted and subtracts it from 'a' to get the index for the TireNode.children[array]
    # if you were inputting 'a' that is 'a' - 'a' = 0 ; the first spot in the children array
    def get_index(self, char):
        return ord(char) - ord('a')

    # function to insert a given key in the Trie
    def insert(self, key):
        # key doesn't exsist or typed in 'None'
        if key is None:
            return False

        # convert inserted word to lowercase
        key = key.lower()
        # create variable called `current` to point to the Trie's root node
        current = self.root

        # input thier
        # t is the first letter
        for letter in word:
            index = self.get_index(letter)

            # letter of the inserted `string` is not in our Trie
            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
                print(letter, "was inserted")

            # move along if that letter is already located in our Trie
            current = current.children[index]

        # end of the word once out of the O(n) for loop going through the word
        current.is_last_word = True
        print("'" + key + "' was inserted")

    # function to search a given key from Trie
    def search(self, word):
        if word is None:
            return False

        current = self.root
        word = word.lower()

        for char in word:
            index_char = self.get_index(char)
            if current.children[index_char] is None:
                return False
            current = current.children[index_char]

        if current and current.is_last_word:
            return True

        return False

    def delete_helper(self, current, word, word_length, level):
        self_deleted = False

        if current is None:
            print('{word} not found')
            return self_deleted

        if word_length == level:
            print('We have reached the end of the word')
            # the current node has no children or other words in the trie
            if current.children.count(None) == len(current.children):
                print(f'-Node {current.char} has no children, delete it')
                current = None
                self_deleted = True
            # the current node is a prefix for other words in the trie
            else:
                # change the boolean of is_last_char b/c this specific letter is a stem for other words
                print(f'-Node {current.char} has children, do not delete it')
                current.is_last_char = False
                self_deleted = False
        else:
            index = self.get_index(word[level])
            print(f'Traversing to {word[level]}')
            child_node = current.children[index]
            child_deleted = self.delete_helper(
                child_node, word, word_length, level+1)
            # this is the return from the recursion either self_deleted is T or F
            # only executes when T
            if child_deleted:
                if current.char is '':
                    print(f'--Cannot Delete Because We Are At The Root')
                    current.children[index] = None
                else:
                    print(f'Delete link from {current.char} to {word[level]}')
                    current.children[index] = None
                    # if there are still words in current.children[] then we can not delete
                    if current.is_last_char:
                        print(f'--Cannot Delete {current.char} because it\'s part of a word\'s end')
                        self_deleted = False
                    # if we hit the boolean true of the last character than its part of another word
                    elif current.children.count(None) != len(current.children):
                        print(f'--Cannot Delete {current.char} because it is part of other words in Trie')
                        self_deleted = False
                    # its not the last letter of a word and/it has no more branches to other words from the last letter
                    else:
                        print(f'--Deleted {current.char}')
                        current = None
                        self_deleted = True
            else:
                self_deleted = False

        return self_deleted

    # function to delete a given key from Trie
    def delete(self, word):
        if not self.root or not word:
            print('Instantialization Error')
            return
        word = word.lower()
        self.delete_helper(self.root, word, len(word), 0)


list_of_words = ['bed', 'bedroom', 'the', 'thier', 'none',
                 'zero', 'absolute', 'apple', 'zebra', 'barnacle', 'me', 'i']

trie = Trie()

for word in list_of_words:
    trie.insert(word)

print(ord('t') - ord('a'))  # 19
print(trie.search('me'))
trie.delete('me')
print(trie.search('me'))
