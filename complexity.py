"""
The PyList append method, a sequence of n append
operations on a PyList object, starting with an empty list, takes O(n) time meaning
that individual operations must not take longer than O(1) time. How can this be true?
Whenever the list runs out of space a new list is allocated and all the old elements
are copied to the new list. Clearly, copying n elements from one list to another takes
longer than O(1) time. Understanding how append could exhibit O(1) complexity
relies on computing the amortized complexity of the append operation. Technically,
when the list size is doubled the complexity of append is O(n).
"""
class PyList:
    # The size is an initial number of locations for the list object. 
    # The numItems instance variable keeps track of how many elements are currently stored
    # in the list since self.items may have empty locations at the end.
    def __init__(self, size=1):
        self.items = [None] * size
        self.numItems = 0
    
    def append(self, item):
        if self.numItems ==len(self.items):
            # make the list bigger by allocating a new list and copying
            # all the elements over to the new list.
            newlst = [None] * self.numItems * 2
            for k in range(len(self.items)):
                newlst[k] = self.items[k]

            self.items = newlst

        self.items[self.numItems] = item
        self.numItems += 1

def main():
    p = PyList()

    for k in range(10):
        p.append(k)

    print(p.items)
    print(p.numItems)
    print(len(p.items))

if __name__ =="__main__":
    main()
        
"""
Expected Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 
42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
None, None, None, None, None, None, None, None, None, None, None, None, None, None]
100
128
"""
            
        