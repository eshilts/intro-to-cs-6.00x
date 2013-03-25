class Queue(object):
    def __init__(self):
        self.line = []

    def insert(self, element):
        """Inserts element to the back of the queue."""
        self.line.append(element)

    def remove(self):
        """ Removes (or 'pops') one element from your Queue and returns it. If
        the queue is empty, raises a ValueError."""
        if len(self.line) == 0:
            raise ValueError, "No more elements in the queue to remove."

        frontOfLine = self.line[-1]
        self.line = self.line[:-1]
        return frontOfLine


queue = Queue()
queue.insert(5)
queue.insert(6)
print queue.remove()
queue.insert(7)
print queue.remove()
print queue.remove()
print queue.remove()
