#!/usr/bin/env python
# coding: utf-8

# In[7]:


class RoomObject:
    def __init__(self, name):
        self.name = name
        self.location = None

    def place(self, location):
        self.location = location


class Table(RoomObject):
    pass


class Chair(RoomObject):
    pass


class Window(RoomObject):
    pass


class Board(RoomObject):
    pass


class Chalk(RoomObject):
    pass


class Door(RoomObject):
    pass


class Room:
    def __init__(self):
        self.tables = [Table(f"Table {i+1}") for i in range(10)]
        self.chairs = [Chair(f"Chair {i+1}") for i in range(10)]
        self.windows = [Window(f"Window {i+1}") for i in range(4)]
        self.board = Board("Board")
        self.chalk = Chalk("Chalk")
        self.door = Door("Door")

        self.set_positions()

    def set_positions(self):
        self.tables[0].place("center")
        self.chairs[0].place("near Table 1")
        self.chairs[1].place("near Table 1")
        self.windows[0].place("left")
        self.windows[1].place("right")
        self.board.place("on the wall")
        self.chalk.place("on the Board")
        self.door.place("opposite the Board")


# Пример использования:
room = Room()

for table in room.tables:
    print(f"{table.name} находится {table.location}")

for chair in room.chairs:
    print(f"{chair.name} находится {chair.location}")

for window in room.windows:
    print(f"{window.name} находится {window.location}")

print(f"{room.board.name} находится {room.board.location}")
print(f"{room.chalk.name} находится {room.chalk.location}")
print(f"{room.door.name} находится {room.door.location}")


# In[ ]:




