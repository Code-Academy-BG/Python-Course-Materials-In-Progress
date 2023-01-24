from oop.exercise.table.chair import Chair


class Table:
    def __init__(self, material, places):
        self.material = material
        self.places = places
        self._seats = {key: Chair() for key in range(1, places + 1)}

    def get_is_seat_free(self, seat_id):
        if self.is_place_valid(seat_id):
            if self._seats[seat_id].is_free:
                return True
            print(f"Chair {seat_id} is not free")
        return False

    def is_table_full(self):
        return all(not seat.is_free for seat in self._seats.values())

    def is_place_valid(self, chair_id):
        return 1 <= chair_id <= len(self._seats)

    def place_person(self, chair_id, client_name, *args):
        if self.is_table_full():
            print("Table is full")
            return

        if self.get_is_seat_free(chair_id):
            self._seats[chair_id].sit_on(client_name)

    def free_place(self, chair_id):
        if self.get_is_seat_free(chair_id):
            print("Place is already free")
            return
        self._seats[chair_id].sit_off()

    def free_places(self):
        return sum(1 for seat in self._seats.values() if seat.is_free)

    def __repr__(self):
        repr_message = [
            f"\nOn seat {seat_id} sits: {self._seats[seat_id].person_on}"
            for seat_id in self._seats
        ]
        return f'<Table seats status {"".join(repr_message)}>'

    def __str__(self):
        return f"Table made of {self.material} has {self.free_places()} places free."


table = Table("wood", 10)

table.place_person(1, "Pesho")
# table.place_person(2, "Stamat")
# table.place_person(3, "Ivan")
# table.place_person(4, "Jane")
# table.place_person(6, "nqkoi")

print(table.__repr__())

