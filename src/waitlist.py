class Waitlist:
    def __init__(self):
        self._queue = []

    def join(self, name):
        """Add a name to the end of the waitlist."""
        self._queue.append(name)

    def to_list(self):
        """Return a copy of the waitlist."""
        return list(self._queue)

    def __len__(self):
        """Return the number of people in the waitlist."""
        return len(self._queue)

    def find(self, name):
        """Return True if name is in the waitlist, otherwise False."""
        return name in self._queue

    def cancel(self, name):
        """Remove the first occurrence of `name`. Return True if removed, else False."""
        if name in self._queue:
            self._queue.remove(name)
            return True
        return False

    def bump(self, name):
        """Move `name` to the front. Return True if bumped, else False."""
        if name in self._queue:
            self._queue.remove(name)
            self._queue.insert(0, name)
            return True
        return False
