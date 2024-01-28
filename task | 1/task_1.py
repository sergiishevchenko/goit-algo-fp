class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_to_start(self, data):
        node = Node(data)

        node.next = self.head
        self.head = node

    def insert_to_end(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def insert_after(self, previous_node: Node, data):
        if previous_node is None:
            return
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def insertion_sort(self):
            if self.head is None or self.head.next is None:
                return

            sorted_head = None
            current = self.head

            while current:
                next_node = current.next

                if sorted_head is None or sorted_head.data >= current.data:
                    current.next = sorted_head
                    sorted_head = current
                else:
                    temp = sorted_head
                    while temp.next and temp.next.data < current.data:
                        temp = temp.next
                    current.next = temp.next
                    temp.next = current

                current = next_node

            self.head = sorted_head

    def search(self, data: int):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def delete(self, key: int):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:
            return
        previous.next = current.next
        current = None

    def print_lst(self):
        current = self.head
        list = []

        while current:
            list.append(current.data)
            current = current.next
        print(list)
        return list

    def reverse(self):
        current = self.head
        previous = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def sort(self):
        current = self.head

        if current is None:
            return
        else:
            while current.next:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                current = current.next

    def merge_sorted_lists(self, in_list):
        current = LinkedList()

        list_1 = self
        list_2 = in_list

        while list_1.head is not None and list_2.head is not None:
            if list_1.head.data < list_2.head.data:
                current.insert_to_end(list_1.head.data)
                list_1.head = list_1.head.next
            else:
                current.insert_to_end(list_2.head.data)
                list_2.head = list_2.head.next

        if list_1.head is not None:
            current.insert_to_end(list_1.head.data)
        elif list_2.head is not None:
            current.insert_to_end(list_2.head.data)

        return current


def main():
    linked_list = LinkedList()

    linked_list.insert_to_start(5)
    linked_list.insert_to_start(10)
    linked_list.insert_to_start(15)
    linked_list.print_lst()

    linked_list.insert_to_end(15)
    linked_list.insert_to_end(25)
    linked_list.print_lst()

    linked_list.insert_after(linked_list.head.next, 15)
    linked_list.print_lst()

    linked_list.delete(15)
    linked_list.print_lst()

    print(f"Search for 25: {linked_list.search(25).data if linked_list.search(25) else None}")

    linked_list.reverse()
    linked_list.print_lst()

    linked_list.insertion_sort()
    linked_list.print_lst()

    linked_list_2 = LinkedList()

    linked_list_2.insert_to_end(15)
    linked_list_2.insert_to_end(10)
    linked_list_2.insert_to_end(14)
    linked_list_2.insertion_sort()
    linked_list_2.print_lst()

    linked_list.merge_sorted_lists(linked_list_2)


if __name__ == "__main__":
    main()
