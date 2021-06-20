class Node:

    def __init__(self, data) -> None:
        self.previous = None
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return self.data


class DLinkedList:
    def __init__(self, nodes) -> None:
        self.head = None
        if nodes is not None:
            current_node = Node(nodes.pop(0))
            self.head = current_node
            for elem in nodes:
                current_node.next = Node(elem)
                temporarily_previous = current_node
                current_node = current_node.next
                current_node.previous = temporarily_previous

    def insert(self, data, place=-1):
        new_node = Node(data)
        if place == 0:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            return True
        count = 1
        node = self.head
        while node:
            if count == place or not node.next:
                new_node.next = node.next
                new_node.previous = node
                node.next = new_node
                if new_node.next:
                    next_node = new_node.next
                    next_node.previous = new_node
                return True
            count += 1
            node = node.next

    def length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def find(self, searched_data):
        node = self.head
        while node is not None:
            if node.data == searched_data:
                return node
            node = node.next
        return None

    def remove_data(self, data):
        '''
        Remove first element with data and return True
        if success else return False
        '''
        previous_node = None
        node = self.head
        while node is not None:
            if node.data == data:
                if previous_node is None:
                    self.head = node.next
                    self.head.previous = None
                    del node
                    return True
                previous_node.next = node.next
                if node.next:
                    next_node = node.next
                    next_node.previous = previous_node
                del node
                return True
            previous_node = node
            node = node.next
        return False

    def remove(self, position=None):
        if position == 0:
            self.head = self.head.next
            self.head.previous = None
            return True
        node = self.head
        count = 0
        while node:
            if count == position or (not node.next and not position):
                previous_node = node.previous
                next_node = node.next
                del node
                previous_node.next = next_node
                if next_node:
                    next_node.previous = previous_node
                return True
            node = node.next
            count += 1
        return False

    def show_neighbors(self, position):
        node = self.head
        count = 0
        while node:
            if count == position:
                print(f"{node.previous} <-> {node} <-> {node.next}")
                break
            node = node.next
            count += 1
        else:
            print("Position is out of range")

    def __str__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " <-> ".join(nodes)


if __name__ == "__main__":
    l = DLinkedList(['a', "b", "c", "d"])
    print(l.insert("z"))
    print(l)
    print(l.insert("k", 2))
    print(l)
    print(l.length())
    print(l.remove(0))
    print(l.remove(6))
    print(l)
    l.show_neighbors(1)