"""

Module to handle a Hotel Reservation System

"""

# pylint: disable=R0903


class Reservation:
    """Class representing a reservation in a hotel."""

    reservation_counter: int = 1

    def __init__(self,
                 check_in_date: str,
                 check_out_date: str,
                 id_hotel: int,
                 id_customer: int) -> None:
        """Initialize a Reservation object.

        Args:
            check_in_date (str): Check-in date in the format 'YYYY-MM-DD'.
            check_out_date (str): Check-out date in the format 'YYYY-MM-DD'.
            id_hotel (int): The ID of the hotel.
            id_customer (int): The ID of the customer.
        """
        self.reservation_id: int = Reservation.reservation_counter
        Reservation.reservation_counter += 1
        self.check_in_date: str = check_in_date
        self.check_out_date: str = check_out_date
        self.id_hotel: int = id_hotel
        self.id_customer: int = id_customer


class Customer:
    """Class representing a customer in a hotel."""

    customer_counter: int = 1

    def __init__(self, name: str,
                 age: int,
                 elite_status: bool = False,
                 id_hotel: int = None) -> None:
        """Initialize a Customer object.

        Args:
            name (str): The name of the customer.
            age (int): The age of the customer.
            elite_status (bool): Whether the customer has elite status.
            id_hotel (int): The ID of the hotel.
        """
        self.id_customer: int = Customer.customer_counter
        Customer.customer_counter += 1
        self.name: str = name
        self.age: int = age
        self.elite_status: bool = elite_status
        self.id_hotel: int = id_hotel

    @classmethod
    def create_customer(cls, name: str,
                        age: int,
                        elite_status: bool = False,
                        id_hotel: int = None) -> 'Customer':
        """Create a new Customer instance.

        Args:
            name (str): The name of the customer.
            age (int): The age of the customer.
            elite_status (bool): Whether the customer has elite status.
            id_hotel (int): The ID of the hotel. Defaults to None.

        Returns:
            Customer: A new Customer instance.
        """
        return cls(name, age, elite_status, id_hotel)

    def delete_customer(self, customer_list: list) -> None:
        """Delete the customer from the provided list.

        Args:
            customer_list:List of customers to delete the customer.
        """
        customer_list.remove(self)

    def display_info(self) -> None:
        """Display information about the customer."""
        print(f"Customer ID: {self.id_customer}")
        print(f"Customer: {self.name}")
        print(f"Age: {self.age}")
        print(f"Elite Status: {'Yes' if self.elite_status else 'No'}")

    def display_customer_info(self) -> None:
        """Display information about the customer."""
        self.display_info()

    def update_elite_status(self, new_status: bool) -> None:
        """Update the elite status of the customer.

        Args:
            new_status (bool): The new elite status.
        """
        self.elite_status = new_status


class Hotel:
    """Class representing a hotel."""

    def __init__(self, id_hotel: int,
                 name: str,
                 address: str,
                 capacity: int) -> None:
        """Initialize a Hotel object.

        Args:
            id_hotel (int): The ID of the hotel.
            name (str): The name of the hotel.
            address (str): The address of the hotel.
            capacity (int): The capacity of the hotel.
        """
        self.id_hotel: int = id_hotel
        self.name: str = name
        self.address: str = address
        self.stars: int = 0
        self.capacity: int = capacity
        self.reservations: list = []

    def create_hotel(self, name: str,
                     address: str,
                     stars: int,
                     capacity: int) -> None:
        """Create or modify a hotel with the provided information.

        Args:
            name (str): The name of the hotel.
            address (str): The address of the hotel.
            stars (int): The star rating of the hotel.
            capacity (int): The capacity of the hotel.
        """
        self.name = name
        self.address = address
        self.stars = stars
        self.capacity = capacity

    def delete_hotel(self) -> None:
        """Delete the hotel."""
        del self

    def display_info(self) -> None:
        """Display information about the hotel."""
        print(f"Hotel ID: {self.id_hotel}")
        print(f"Hotel: {self.name}")
        print(f"Address: {self.address}")
        print(f"Stars: {self.stars}")
        print(f"Capacity: {self.capacity} guests")
        print("Reservations:")
        for reservation in self.reservations:
            one = f"{reservation.reservation_id},{reservation.guest_name}, "
            two = f"{reservation.check_in_date},{reservation.check_out_date}"
            print(one + two)

    def modify_info(self, name: str = None,
                    address: str = None,
                    stars: int = None,
                    capacity: int = None) -> None:
        """Modify the information of the hotel.

        Args:
            name (str): The new name of the hotel. Defaults to None.
            address (str): The new address of the hotel. Defaults to None.
            stars (int): The new star rating of the hotel. Defaults to None.
            capacity (int): The new capacity of the hotel. Defaults to None.
        """
        if name:
            self.name = name
        if address:
            self.address = address
        if stars:
            self.stars = stars
        if capacity:
            self.capacity = capacity

    def reserve_room(self, check_in_date: str, check_out_date: str) -> int:
        """Reserve a room in the hotel.

        Args:
            check_in_date (str): Check-in date in the format 'YYYY-MM-DD'.
            check_out_date (str): Check-out date in the format 'YYYY-MM-DD'.

        Returns:
            int: The ID of the reservation.
        """
        reservation = Reservation(check_in_date,
                                  check_out_date,
                                  self.id_hotel,
                                  len(self.reservations) + 1)
        self.reservations.append(reservation)
        return reservation.reservation_id

    def cancel_reservation(self, reservation_id: int) -> bool:
        """Cancel a reservation in the hotel.

        Args:
            reservation_id (int): The ID of the reservation to be canceled.

        Returns:
            bool: True if the reservation is canceled, False otherwise.
        """
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                self.reservations.remove(reservation)
                return True
        return False
