#!/usr/bin/env python
# encoding: utf-8

from main import Queue


def test():
    q = Queue()
    print q.empty()
    print q.peek()
    print q.pop()
    print q.push(1)
    print q.push(2)
    print q.empty()
    print q.peek()
    print q.pop()

test()
