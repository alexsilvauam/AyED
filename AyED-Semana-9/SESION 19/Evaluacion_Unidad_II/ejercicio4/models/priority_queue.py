class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, name, priority):
        self.queue.append((name, priority))
        self.queue.sort(key=lambda x: x[1])  # Ordenar por prioridad

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def get_queue(self):
        return self.queue 