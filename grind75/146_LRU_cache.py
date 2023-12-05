class ListNode:
    def __init__(self):
        self.val = 0
        self.key = 0
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.mapping = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _delete_node(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before

    def _add_node_to_end(self, node) -> None:
        last_node = self.tail.prev
        last_node.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = last_node

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1

        # TODO: update the position of node in linkedlist
        # delete node from the original position
        node = self.mapping[key]
        self._delete_node(node)
        # add node to the last of the linkedlist
        self._add_node_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.mapping:
            node = ListNode()
            node.key = key
            node.val = value
            self.mapping[key] = node
            self.size += 1

            # TODO: add node to the end of the list
            self._add_node_to_end(node)
            # TODO: check if the size exceeds self.capacity. 
            if self.size > self.capacity:
            # TODO: if it exceeds, delete the oldest node from list and mapping, self.size -= 1
                curr = self.head
                del self.mapping[self.head.next.key]
                # self._delete_from_top()
                self._delete_node(self.head.next)
                self.size -= 1
        
        else:
            self.mapping[key].val = value
            # TODO: move the node to the end of the list
            # delete the node from its original position in the list
            self._delete_node(self.mapping[key])
            # add the node to the end of the list
            self._add_node_to_end(self.mapping[key])