class ParkingSlot:
    def __init__(self, slot_id, slot_number, vehicle_type, is_occupied, assigned_vehicle):
        self.slot_id = slot_id
        self.slot_number = slot_number
        self.vehicle_type = vehicle_type
        self.is_occupied = is_occupied
        self.assigned_vehicle = assigned_vehicle
