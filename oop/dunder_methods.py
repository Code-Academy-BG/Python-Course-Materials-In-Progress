class ClassRoom:
    def __init__(self):
        self._start_seat = 0
        self.seats = range(24)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            seat = self.seats[self._start_seat]
            self._start_seat += 1
            return seat
        except StopIteration:
            return


class_room = ClassRoom()

# This is causing IndexError after printing out the last of seats.
for seat in class_room:
    print(seat)
