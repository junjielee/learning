#!/usr/bin/env python
# encoding: utf-8


class Queue(object):
    """
    two direction queue
    """
    # initialize your data structure here.
    def __init__(self):
        self.queue = []
        self.size = 0

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)
        self.size += 1

    # @return nothing
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.pop(0)

    # @return nothing
    def pop_from_back(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.pop(self.size)

    # @return an integer
    def peek(self):
        if self.size > 0:
            return self.queue[0]

    # @return an boolean
    def empty(self):
        return self.size == 0

    # @return queue's size
    def size(self):
        return self.size
