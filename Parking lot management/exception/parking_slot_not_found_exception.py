class ParkingSlotNotFoundException(Exception):
    def __init__(self, message="Parking slot not found"):
        super().__init__(message)
