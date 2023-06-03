#!/usr/bin/python3

"""Contains two classes Node and SinglyLinkedList."""


class Node:
    """a class Node"""
    def __init__(self, data, next_node=None):
        """Initialize class node.

        Args:
            data (int): integer value to be stored in the list
            next_node (:obj:`Node`:optional): object of type Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """property data.

        an integer value, else raise an exception
        """
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """property next_node.

        a value of type Node.
        can be None or must be a Node, else raise an exception
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (isinstance(value, Node) or (value is None)):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """a singly linked list of Node.

    """
    def __init__(self):
        """class initialization"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position"""
        a = self.__head
        n = Node(value)
        if (a is None):
            self.__head = n
        elif (a.data > value):
            n.next_node = a
            self.__head = n
        else:
            while (a):
                if (a.next_node is None):
                    a.next_node = n
                    break
                elif (a.next_node.data > value):
                    c = a.next_node
                    a.next_node = n
                    n.next_node = c
                    break
                a = a.next_node

    def __str__(self):
        """printable output"""
        a = self.__head
        string = ""
        if (a):
            while (a.next_node):
                y = a.data
                a = a.next_node
                string += f"{y}\n"
            else:
                y = a.data
                string += f"{y}"
        return string
