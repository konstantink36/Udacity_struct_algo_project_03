# HTTPRouter using a Trie

# Router trie node with link to children dictionary:
class RouteTrieNode:
    def __init__(self, handler = None):
        self.handler = handler
        self.children = {}

    #def insert(self, path_split, handler):
         #self.children[path_piece] = RouteTrieNode(handler)

# Initialize the router trie with root node and root node handler
class RouteTrie:
    def __init__(self, handler = None, handler2 = None):  # root node handler = home page?
        self.root = RouteTrieNode(handler)
        self.notfound = RouteTrieNode(handler2)

    # add nodes to an url path and assign handler to the leaf node of this path
    def insert(self, path_split, handler):
        current_node = self.root
        for x in path_split:
            if x not in current_node.children:			
                current_node.children[x] = RouteTrieNode(None) 
            current_node = current_node.children[x]
        current_node.handler = handler              

    # find the node for a given path and return its handler
    def find(self, path_split):
        current_node = self.root
        for x in path_split:
            if x not in current_node.children:
                return self.notfound.handler
            current_node = current_node.children[x]  
        if current_node.handler != None:
            return current_node.handler
        else: 
            return self.notfound.handler
    
 
#Router class for wrapping up the Trie. Create instance of router trie with handler for root node 
class Router:
    def __init__(self, handler, handler2):     			
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routetrie = RouteTrie(handler, handler2)
        
    # Add a handler for a path. Split the path and pass the pass parts as a list to the RouteTrie
    def add_handler(self, path, handler):         
        path_split = self.split_path(path)
        self.routetrie.insert(path_split, handler)

    # lookup path and return handler
    def lookup(self, path):
        path_split = self.split_path(path)
        return self.routetrie.find(path_split)

    # helper function to split the path in parts seapareted by "/". Returns list with path parts
    def split_path(self, path):   
        path_split = path.split("/")
        path_split = list(filter(None, path_split))   # remove empty strings from list with path parts
        return path_split
        


print("Test 1:")

# create the router and add a route
router = Router("root handler", "not found handler") # create Router
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) 						# prints 'root handler'
print(router.lookup("/home")) 						# prints 'not found handler' 
print(router.lookup("/home/about")) 					# prints 'about handler'
print(router.lookup("/home/about/")) 					# prints 'about handler' 
print(router.lookup("/home/about/me")) 					# prints 'not found handler' 


print("Test 2:")

# create the router and add a route
router1 = Router("root handler", "not found handler") 
router1.add_handler("/home/udacity", "udacity handler")  
router1.add_handler("/home/udacity/projects/project3/problem1", "problem1 handler") 

# some lookups with the expected output
print(router1.lookup("/")) 						# prints 'root handler'
print(router1.lookup("/home/udacity")) 					# prints 'udacity handler'
print(router1.lookup("/home/udacity/projects")) 			# prints 'not found handler' 
print(router1.lookup("/home/udacity/projects/project3/problem1")) 	# prints 'problem1 handler' 
print(router1.lookup("/home/udacity/projects/project3/")) 		# prints 'not found handler' 



print("Test 3:")

# create the router and add a route
router1 = Router("root handler", "not found handler") 
router1.add_handler("/home/animals", "animals handler")  
router1.add_handler("/schemas.microsoft.com/SMI/2016/Windows Settings", "windows handler")  

# some lookups with the expected output
print(router1.lookup("/home/animals/")) 					# prints 'animals handler' 
print(router1.lookup("/schemas.microsoft.com/SMI/2016/Windows Settings/"))	# prints 'windows handler' 
print(router1.lookup("/home/animals/dogs")) 					# prints 'not found handler' 
