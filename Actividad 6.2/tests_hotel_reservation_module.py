import unittest
from datetime import date

from hotel_reservation_module import Hotel, Customer, Reservation

class TestHotelReservationSystem(unittest.TestCase):

    def setUp(self):
        # Create instances of the necessary classes for the tests
        self.hotel = Hotel(1, "Example Hotel", "123 Main St", 100)
        self.customer = Customer.create_customer("John Doe", 30)
        self.reservation = Reservation("2024-03-01", "2024-03-05", 1, 1)

    def test_reserve_room(self):
        # Ensure a room can be reserved successfully
        reservation_id = self.hotel.reserve_room("2024-03-01", "2024-03-05")
        self.assertEqual(len(self.hotel.reservations), 1)

    def test_cancel_reservation(self):
        # Ensure a reservation can be canceled successfully
        self.hotel.reservations.append(self.reservation)
        result = self.hotel.cancel_reservation(self.reservation.reservation_id)
        self.assertTrue(result)
        self.assertEqual(len(self.hotel.reservations), 0)

    def test_create_customer(self):
        # Ensure a customer can be created successfully
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.age, 30)

    def test_update_elite_status(self):
        # Ensure the customer's elite status can be updated successfully
        self.customer.update_elite_status(True)
        self.assertTrue(self.customer.elite_status)

    def test_display_info(self):
        # Ensure information can be displayed correctly
        self.customer.display_info()

    def test_display_customer_info(self):
        # Ensure customer information can be displayed correctly
        self.customer.display_customer_info()

    def test_modify_hotel_info(self):
        # Ensure hotel information can be modified correctly
        self.hotel.modify_info(name="New Name", stars=5)
        self.assertEqual(self.hotel.name, "New Name")
        self.assertEqual(self.hotel.stars, 5)

    def test_delete_customer(self):
        # Ensure a customer can be deleted correctly from the list of customers
        customer_list = [self.customer]
        self.customer.delete_customer(customer_list)
        self.assertEqual(len(customer_list), 0)


if __name__ == '__main__':
    unittest.main()
