# Description: This program solves what is known as the Josephus problem. There is a group of soldiers surrounded by an overwelming force. There is no hope, so they make a pact to commit suicide. They form a circle and a number n is picked from a hat. One of their names is picked at random. Beginning with the solider whose name is picked, they begin to count clockwise around the circle. Whne the count reaches n, that soldier is executed, and the count begins with the next man. The process continues so that each time the count reaches n, a man is removed from the circle. Once a soldier is removed from the circle he is no longer counted. The last soldier remaining was Josephus and instead of taking his life he joined the enemy forces. This program takes a given number n, the ordering of men in the circle, and the man from whom the count begins, to determine the order in which the men are eliminated from the circle and which man escapes. This program uses a circular linked list.

import sys

class Link(object):
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
        
class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None
        
    # Insert an element (value) in the list
    def insert(self,data):
        element = Link(data)
        if self.first is None:
            self.first = element
            self.last = element
        else:
            self.last.next = element
            element.next = self.first
            self.last = element            
            
    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self,data):
        c = None
        if self.first != None:
            c = self.first
            is_found = False
            while not is_found:
                if c.data == data:
                    is_found = True
                else:    
                    c = c.next
                if c == self.first:
                    break
        return c
        
    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete(self,data):
        c = None
        if self.first != None and self.last != None:
            c = self.first
            p = self.last
            is_found = False
            while not is_found:
                if c.data == data:
                    is_found = True
                else:    
                    p = c
                    c = c.next
                if c == self.first:
                  break
            if is_found:
                p.next = c.next
                if c == self.first and c == self.last:
                    self.first = None
                    self.last = None
                elif c == self.first:
                    self.first = c.next
                elif c == self.last:
                    self.last = p
            else:
                c = None
        return c

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after(self,start,n):
        deleted = None
        next_link = None
        if start != None:
            for i in range(1,n):
                start = start.next   
            deleted = start
            next_link = deleted.next
            self.delete(deleted.data)
        return deleted, next_link;
            
    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__ (self):
        s = []
        if self.first != None:
            c = self.first
            while c is not None and c.data != self.last.data:
                s.append(c.data)
                c = c.next
            s.append(c.data)
        return str(s)

def main():
    #read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    #read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    #read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)
    
    # your code
    l = CircularList()
    for x in range(1,num_soldiers+1):
        l.insert(x)
    start = l.find(start_count)
    while l.first != l.last and start != None:
        deleted, start = l.delete_after(start,elim_num)
        if deleted != None:
            print(deleted.data)
    if start != None:
        print(start.data)    
    
if __name__ == "__main__":
    main()
