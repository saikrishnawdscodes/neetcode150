# Logic :
# ========

# You have to design an LRU cache - using linkedlists and hashmaps.

# why LL and hashmaps ? 
# LL -> coz of O(1) deletion and O(1) insertion. 
# Make it a doubly linked list - as moving the cached items to and fro - from most recent to least recent - is easier with a prev and a next ptr.
# IDEA is to store the least recently used item next to head - so that it can easily be accessed and removed; and the most recently used item closer to tail.

# hashmaps - for O(1) retrieval based on keys; and also cuz entries are stored as key val pairs!
# for the problem - only an LRU cache is added - but you add a special node class as well - that contains the nodes for the doubly LL


# for the LRU class - there are 2 util functions - get() and put()
# get () fetches the item from cache if available - but returns -1 if not there, 
# apart from this - it also moves the least fetched item away closer to head - by moving the most recently used item away from head.

# put() - update the key if key exists, else add the new key val pair, if cache capacity is full  - then remove the LRU and then put this in.

# SETUP : 
# =======

# You have the cache itself being implemented as one big hashmap - with keys being the cache keys
# but vals will be pointers to the nodes which form the doubly LL.

# dummy key -> left node
# key 1  -> [val1, next1, prev1] 
# key 2 -> [val2, next2, prev2]
# key 3 -> [val3, next3, prev3]
# dummy key -> right node


# the values themselves are connected to each other!
# We start off with a left and right nodes in between which the key val pairs are added!

# my code - which is not correct! 

class Node:
    def __init__(self, val = None, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0)
        self.right = Node(0)

    

    def get(self, key:int) -> int:
        if key in self.cache:
            current_node = self.cache.key
            node_left_of_cn = self.cache.key.prev
            node_right_of_cn = self.cache.key.next 
            last_node = self.right
            
            node_left_of_cn.next = node_right_of_cn # remove node - linking up the gap
            node_right_of_cn.prev = node_left_of_cn

            last_node.next = current_node  # moving node to MRU
            current_node.prev = last_node

            return self.cache[key]
        else:
            return -1


    def put(self, key:int, value:int) -> None:
        if key in self.cache:
            self.cache[key] = value
        else:
            if  len(self.cache) >= self.capacity :  # eviction needed
                # eviction of LRU
                node_to_be_evicted = self.left.next
                node_right_of_evict_node = node_to_be_evicted.next
                self.left.next = node_right_of_evict_node
                node_right_of_evict_node.prev = self.left        

            new_node = Node(value)   # adding new node
            current_MRU = self.right.prev
            self.right.prev = new_node
            new_node.prev = current_MRU
            new_node.next = self.right
            self.cache[key] = new_node
                
                

# correct code : 

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# TC: O(1) for each get() and put()
# SC : O(n)




# 3. Built-In Data Structure - implementation using OrderedDict


from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)


# the move_to_end() and popitem() functions implement what we coded above!
# TC: O(1) for each get() and put()
# SC : O(n)