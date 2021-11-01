# Trie structure to store dynamic set of strings and with the ability to list suffixes to implement an autocomplete feature
# For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().


class TrieNode:
        ## Initialize this node in the Trie
    def __init__(self, string = ""):
        self.string = string  		
        self.is_word = False
        self.children = {}

    def find_words(self, node, suffixes_list) :	
	#helper method to recursively find suffixes
        if node.is_word:				# if node contains complete word
            suffix = node.string[len(self.string):]    # suffix is complete word minus prefix (self is prefix node)
            suffixes_list.append(suffix)
        for y in node.children:			
            self.find_words(node.children[y], suffixes_list)		

    def suffixes(self):
    ## Recursive function that collects the suffix for all complete words below this point	
        suffixes_list = list()
        self.find_words(self, suffixes_list)		 
        suffixes_list = list(filter(None, suffixes_list))     #remove empty strings
        return suffixes_list


class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()
        self.notfound = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for x, char in enumerate(word):				
            if char not in current_node.children:         
                prefix = word[0:x+1]			# keeping track of prefix added so far 
                current_node.children[char] = TrieNode(prefix)  
            current_node = current_node.children[char]    
        current_node.is_word = True                       


    def find(self, prefix):
        ## Find the Trie node that represents this prefix and return that node
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return self.notfound			#if prefix does not exist, return not found node
            current_node = current_node.children[char]          
        return current_node		



# Tests below

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

prefixnode = MyTrie.find("f")
print(prefixnode.suffixes())
# prints  ['un', 'unction', 'actory']

prefixnode = MyTrie.find("tri")
print(prefixnode.suffixes())
# prints  ['e', 'gger', 'gonometry', 'pod']

prefixnode = MyTrie.find("ant")
print(prefixnode.suffixes())
# prints  ['hology', 'agonist', 'onym']

prefixnode = MyTrie.find("")
print(prefixnode.suffixes())
# prints ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

prefixnode = MyTrie.find(" ")
print(prefixnode.suffixes())
# prints []

prefixnode = MyTrie.find("None")
print(prefixnode.suffixes())
# prints []

prefixnode = MyTrie.find("g")
print(prefixnode.suffixes())
# prints  []
