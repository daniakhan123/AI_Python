
import time

class HospitalDeliveryRobot:
    def __init__(self):
        self.locations = {
            'storage': "Medicine Storage",
            'nurse_station': "Nurse Station",
            'rooms': {101: "Patient 101", 102: "Patient 102", 103: "Patient 103"}
        }
        self.medicine_schedule = {
            101: "Painkillers",
            102: "Antibiotics",
            103: "Vitamins"
        }
        self.current_location = 'storage'

    def move_to(self, location):
        print(f"Moving to {self.locations.get(location, location)}...")
        time.sleep(1)
        self.current_location = location
        print(f"Arrived at {self.locations.get(location, location)}")

    def pick_up_medicine(self, room_number):
        print(f"Picking up {self.medicine_schedule[room_number]} for Room {room_number}...")
        time.sleep(1)
        print(f"{self.medicine_schedule[room_number]} picked up!")

    def scan_patient_id(self, room_number):
        print(f"Scanning patient ID in Room {room_number}...")
        time.sleep(1)
        print(f"Patient {room_number} ID verified!")

    def deliver_medicine(self, room_number):
        self.move_to(room_number)
        self.scan_patient_id(room_number)
        print(f"Delivering {self.medicine_schedule[room_number]} to Patient {room_number}...")
        time.sleep(1)
        print(f"Medicine delivered to Patient {room_number}!")

    def alert_staff(self, message):
        self.move_to('nurse_station')
        print(f"Alerting staff: {message}")
        time.sleep(1)
        print("Staff alerted successfully!")

    def start_delivery(self):
        for room_number in self.medicine_schedule:
            self.move_to('storage')
            self.pick_up_medicine(room_number)
            self.deliver_medicine(room_number)
        print("All medicine deliveries completed!")

robot = HospitalDeliveryRobot()
robot.start_delivery()
