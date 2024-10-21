# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Import the TicketService class from ticket_service module
# main.py
if __name__ == "__main__":
    from ticket_service import TicketService

    def main():
        ticket_service = TicketService()

        while True:
            print("\nCustomer Service Ticket Tracker")
            print("1. Open a new service ticket")
            print("2. Update ticket status")
            print("3. Display all tickets")
            print("4. Display tickets by status")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")

            try:
                if choice == "1":
                    customer_name = input("Enter customer name: ")
                    issue_description = input("Enter issue description: ")
                    ticket_service.open_new_ticket(customer_name, issue_description)
                elif choice == "2":
                    ticket_id = input("Enter ticket ID: ")
                    new_status = input("Enter new status (open/closed): ")
                    ticket_service.update_ticket_status(ticket_id, new_status.lower())
                elif choice == "3":
                    print("\nAll Tickets:")
                    ticket_service.display_all_tickets()
                elif choice == "4":
                    filter_status = input("Enter status to filter by (open/closed): ")
                    ticket_service.display_all_tickets(filter_status.lower())
                elif choice == "5":
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    raise ValueError("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    main()