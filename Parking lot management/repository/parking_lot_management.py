from model.parking_slot import ParkingSlot
from exception.parking_slot_not_found_exception import ParkingSlotNotFoundException
from util.db_util import DBConnection

class ParkingLotManagement:
    def __init__(self):
        self.db = DBConnection()
        self.cursor = self.db.get_cursor()

    def add_slot(self, slot_number, vehicle_type, is_occupied, assigned_vehicle):
        self.cursor.execute(
            "INSERT INTO ParkingSlots (slot_number, vehicle_type, is_occupied, assigned_vehicle) VALUES (?, ?, ?, ?)",
            (slot_number, vehicle_type, is_occupied, assigned_vehicle)
        )
        self.db.commit()

    def delete_slot(self, slot_id):
        self.cursor.execute("DELETE FROM ParkingSlots WHERE slot_id = ?", (slot_id,))
        if self.cursor.rowcount == 0:
            raise ParkingSlotNotFoundException()
        self.db.commit()
        return True

    def update_occupancy(self, slot_id, is_occupied, assigned_vehicle):
        self.cursor.execute(
            "UPDATE ParkingSlots SET is_occupied = ?, assigned_vehicle = ? WHERE slot_id = ?",
            (is_occupied, assigned_vehicle, slot_id)
        )
        if self.cursor.rowcount == 0:
            raise ParkingSlotNotFoundException()
        self.db.commit()

    def update_slot(self, slot_id, slot_number=None, vehicle_type=None):
        query = "UPDATE ParkingSlots SET "
        params = []
        if slot_number:
            query += "slot_number = ?, "
            params.append(slot_number)
        if vehicle_type:
            query += "vehicle_type = ?, "
            params.append(vehicle_type)
        query = query.rstrip(", ") + " WHERE slot_id = ?"
        params.append(slot_id)

        self.cursor.execute(query, tuple(params))
        if self.cursor.rowcount == 0:
            raise ParkingSlotNotFoundException()
        self.db.commit()
        return True

    def get_all_slots(self):
        self.cursor.execute("SELECT * FROM ParkingSlots")
        return [ParkingSlot(*row) for row in self.cursor.fetchall()]

    def search_slot(self, slot_number):
        self.cursor.execute("SELECT * FROM ParkingSlots WHERE slot_number LIKE ?", ('%' + slot_number + '%',))
        rows = self.cursor.fetchall()
        if not rows:
            raise ParkingSlotNotFoundException()
        return [ParkingSlot(*row) for row in rows]

    def filter_by_type(self, vehicle_type):
        self.cursor.execute("SELECT * FROM ParkingSlots WHERE vehicle_type = ?", (vehicle_type,))
        return [ParkingSlot(*row) for row in self.cursor.fetchall()]

    def close_connection(self):
        self.db.close()
