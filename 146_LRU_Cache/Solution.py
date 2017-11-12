from typing import Dict

class LLNode(object):

    def __init__(self, key, val, prev_node=None, next_node=None):
        self.key = key
        self.val = val
        self.prev_node = prev_node # type: LLNode
        self.next_node = next_node # type: LLNode


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity # type: int
        self.head = None # type: LLNode
        self.tail = None # type: LLNode
        self.nodes = {} # type: Dict[int, LLNode]

    def _move_to_front(self, key):
        """
        :type key: int
        """
        if key in self.nodes:
            node = self.nodes[key]
            if node != self.head:
                if node == self.tail:
                    self.tail = node.prev_node
                    node.prev_node.next_node = None
                else:
                    node.prev_node.next_node = node.next_node
                    node.next_node.prev_node = node.prev_node
                node.next_node = self.head
                self.head.prev_node = node
                node.prev_node = None
                self.head = node
            return node


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodes:
            return self._move_to_front(key).val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.nodes:
            node = self._move_to_front(key)
            node.val = value
        elif len(self.nodes) == self.capacity:
            key_to_evict = self.tail.key
            node = self._move_to_front(key_to_evict)
            self.nodes.pop(key_to_evict)
            node.key = key
            node.val = value
            self.nodes[key] = node
        elif not self.nodes:
            new_node = LLNode(key, value)
            self.head = new_node
            self.tail = new_node
            self.nodes[key] = new_node
        else:
            new_node = LLNode(key, value, next_node=self.head)
            self.head.prev_node = new_node
            self.head = new_node
            self.nodes[key] = new_node


        
        
if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1)) # returns 1
    cache.put(3, 3) # evicts key 2
    print(cache.get(2)) # returns - 1(not found)
    cache.put(4, 4) # evicts key 1.
    print(cache.get(1)) # returns - 1(not found)
    print(cache.get(3)) # returns 3
    print(cache.get(4)) # returns 4