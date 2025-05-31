from repository.parking_lot_management import ParkingLotManagement
from exception.parking_slot_not_found_exception import ParkingSlotNotFoundException

def main():
    plm = ParkingLotManagement()
    while True:
        print("\n1. Add Slot\n2. Update Occupancy\n3. Delete Slot\n4. View All Slots\n5. Search Slot\n6. Filter by Type\n7. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                slot_number = input("Enter slot number: ")
                vehicle_type = input("Enter vehicle type: ")
                is_occupied = input("Is occupied (1/0): ") == '1'
                assigned_vehicle = input("Enter assigned vehicle: ")
                plm.add_slot(slot_number, vehicle_type, is_occupied, assigned_vehicle)
                print("Slot added successfully.")
            elif choice == '2':
                slot_id = int(input("Enter slot ID: "))
                is_occupied = input("Is occupied (1/0): ") == '1'
                assigned_vehicle = input("Enter assigned vehicle: ")
                plm.update_occupancy(slot_id, is_occupied, assigned_vehicle)
                print("Occupancy updated.")
            elif choice == '3':
                slot_id = int(input("Enter slot ID to delete: "))
                plm.delete_slot(slot_id)
                print("Slot deleted.")
            elif choice == '4':
                slots = plm.get_all_slots()
                for slot in slots:
                    print(vars(slot))
            elif choice == '5':
                keyword = input("Enter partial slot number: ")
                slots = plm.search_slot(keyword)
                for slot in slots:
                    print(vars(slot))
            elif choice == '6':
                v_type = input("Enter vehicle type to filter (e.g., Bike): ")
                slots = plm.filter_by_type(v_type)
                for slot in slots:
                    print(vars(slot))
            elif choice == '7':
                plm.close_connection()
                print("Exiting. Connection closed.")
                break
            else:
                print("Invalid choice.")
        except ParkingSlotNotFoundException as e:
            print("Error:", e)
        except Exception as ex:
            print("Something went wrong:", ex)

if __name__ == "__main__":
    main()
