#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

# 双向循环链表

# 节点
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.pre = None

# 双向循环链表
class CycleDoubleLinkList:
    def __init__(self):
        self._head = Node(None)
        self._head.next = self._head
        self._head.prev = self._head
        self._rear = self._head

    # 插入
    def insert(self, index, value):
        if index < 0:
            print '插入位置有误'
            return
        n = Node(value)
        cur = self._head
        for i in range(index - 1):
            cur = cur.next
            if cur == self._head:
                print '插入位置有误'
                return
        n.next = cur.next
        cur.next.prev = n
        cur.next = n
        n.prev = cur
        if n.next = self.head:
            self._rear = n

    # 删除
    def remove(self,index):
        if self.empty():
            print '链表是空的'
        if index <= 0 and index > self.length():
            print '删除的位置有误'
            return 
        cur = self._head
        for i in range(index - 1):
            cur = cur.next
        n = cur.next
        cur.next.next.prev = cur
        cur.next = cur.next.next
        if cur.next == self._head:
            self._rear = cur
        del n 

    # 判断是否空链表
    def empty(self):
        return self._head.next == self._head

    def travel(self):
        cur = self._head.next
        print '正向输出'
        while cur != self._head:
            print(cur.data)
            cur = cur.next
        print '逆向输出'
        while cur.prev != self._head:
            cur = cur.prev
            print(cur.data)

    def search(self, value):
        cur = self._head.next
        index = 1
        while cur != self._head:
            if cur.data == value:
                print 'index:%d,value:%d'%(index,value)
                return
            cur = cur.next
            index += 1

        print '没有该元素'

    def clear(self):
        cur = self._head.next
        while cur != self._head:
            temp = cur
            cur = cur.next
            del temp
        self._head.next = self._head
        self._head.prev = self._head

    def appendleft(self,value):
        n = Node(value)
        self._head.next.prev = n
        n.next = self._head.next
        self._head.next = n
        n.prev = self._head
        if n.next == self._head:
            self._rear = n

    def appendright(self,value):
        n = Node(value)
        self._rear.next.prev = n
        n.next = self._rear.next
        self._rear.next = n
        n.prev = self._rear
        self._rear = n

    def length(self):
        cur = self._head.next
        count = 0 
        while cur != self._head:
            cur = cur.next
            count += 1
        return count

if __name__ == '__main__':
    link = CycleDoubleLinkList()



