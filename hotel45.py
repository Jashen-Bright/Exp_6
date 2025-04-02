class Hotel:
    def __init__(self, name, total_rooms):
        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms
        #self.booked_rooms = []

    def reserve_room(self, customer_name, room_type):
        if self.available_rooms > 0:
            self.booked_rooms.append({
                'customer': customer_name,
                'room_type': room_type,
                'status': 'Reserved'
            })
            self.available_rooms -= 1
            print(f"Room reserved for {customer_name} ({room_type} room).")
        else:
            print("No rooms available to reserve.")

    def check_in(self, customer_name):
        for booking in self.booked_rooms:
            if booking['customer'] == customer_name and booking['status'] == 'Reserved':
                booking['status'] = 'Checked-in'
                print(f"{customer_name} has checked in.")
                return
        print(f"No reservation found for {customer_name}.")

    def check_out(self, customer_name):
        for booking in self.booked_rooms:
            if booking['customer'] == customer_name and booking['status'] == 'Checked-in':
                booking['status'] = 'Checked-out'
                self.available_rooms += 1
                print(f"{customer_name} has checked out.")
                return
        print(f"{customer_name} has not checked in yet or no reservation found.")
    def show_available_rooms(self):
        print(f"Available rooms: {self.available_rooms}/{self.total_rooms}")

   

    def show_booked_rooms(self):
        print("Booked Rooms:")
        for booking in self.booked_rooms:
            print(f"Customer: {booking['customer']}, Room Type: {booking['room_type']}, Status: {booking['status']}")

hotel = Hotel("Sunshine Hotel", 10)
#fixed context error

hotel.reserve_room("Bright", "Single")
hotel.reserve_room("Mohith", "Double")
hotel.reserve_room("Charlie", "Suite")

hotel.check_in("Bright")
hotel.check_in("Mohith")

hotel.show_available_rooms()

hotel.show_booked_rooms()

hotel.check_out("Bright")
hotel.check_out("Mohith")

hotel.show_available_rooms()
