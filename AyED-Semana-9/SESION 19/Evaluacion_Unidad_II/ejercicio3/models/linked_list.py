class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def add_song(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = new_node
            self.current = self.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_song(self, song):
        if not self.head:
            return False
        
        if self.head.data == song:
            self.head = self.head.next
            if self.current == self.head:
                self.current = self.head
            return True
        
        current = self.head
        while current.next:
            if current.next.data == song:
                if self.current == current.next:
                    self.current = current
                current.next = current.next.next
                return True
            current = current.next
        return False

    def next_song(self):
        if not self.current or not self.current.next:
            return None
        self.current = self.current.next
        return self.current.data

    def previous_song(self):
        if not self.head or not self.current:
            return None
        
        if self.current == self.head:
            return self.current.data
        
        current = self.head
        while current.next != self.current:
            current = current.next
        self.current = current
        return self.current.data

    def get_playlist(self):
        playlist = []
        current = self.head
        while current:
            playlist.append(current.data)
            current = current.next
        return playlist 