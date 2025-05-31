import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from repository.parking_lot_management import ParkingLotManagement


class TestParkingLot(unittest.TestCase):
    def setUp(self):
        self.manager = ParkingLotManagement()

    def test_add_slot(self):
        self.manager.add_slot("P101", "Car", False, "")
        slots = self.manager.search_slot("P101")
        self.assertTrue(any(slot.slot_number == "P101" for slot in slots))

    def tearDown(self):
        self.manager.close_connection()

if __name__ == "__main__":
    unittest.main()
