# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.
# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
import json
import os

class TicketService:
    def __init__(self):
        # Initialize with some sample tickets or load from storage
        self.service_tickets = {}
        self.next_ticket_id = 1
        self.load_tickets()

    def load_tickets(self):
        try:
            if not os.path.exists("tickets.json"):
                # Automatically create a default tickets.json file if it doesn't exist
                self.service_tickets = {
                    "Ticket001": {
                        "Customer": "Alice",
                        "Issue": "Login problem",
                        "Status": "open"
                    },
                    "Ticket002": {
                        "Customer": "Bob",
                        "Issue": "Payment issue",
                        "Status": "closed"
                    },
                    "Ticket003": {
                        "Customer": "Charlie",
                        "Issue": "Account locked",
                        "Status": "open"
                    }
                }
                with open("tickets.json", "w") as file:
                    json.dump(self.service_tickets, file, indent=4)
                print("tickets.json file not found. Created a new one with sample data.")
            else:
                with open("tickets.json", "r") as file:
                    self.service_tickets = json.load(file)
                    if self.service_tickets:
                        self.next_ticket_id = max(int(k.replace("Ticket", "")) for k in self.service_tickets.keys() if k.startswith("Ticket")) + 1
        
        except Exception as e:
            print(f"Error loading tickets from file: {e}")
            exit(1)

    def open_new_ticket(self, customer_name, issue_description):
        try:
            if not customer_name.strip() or not issue_description.strip():
                raise ValueError("Customer name and issue description cannot be empty or just whitespace.")
            if len(customer_name.strip()) < 3 or len(issue_description.strip()) < 5:
                raise ValueError("Customer name must be at least 3 characters and issue description at least 5 characters.")
            
            ticket_id = f"Ticket{str(self.next_ticket_id).zfill(3)}"
            self.service_tickets[ticket_id] = {
                "Customer": customer_name.strip(),
                "Issue": issue_description.strip(),
                "Status": "open"
            }
            self.next_ticket_id += 1
            self.save_tickets()
            print(f"New ticket opened with ID: {ticket_id} for customer '{customer_name.strip()}' with issue: '{issue_description.strip()}'")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_tickets(self):
        try:
            with open("tickets.json", "w") as file:
                json.dump(self.service_tickets, file, indent=4)
        except Exception as e:
            print(f"Error saving tickets to file: {e}")

    def update_ticket_status(self, ticket_id, new_status):
        try:
            if ticket_id not in self.service_tickets:
                raise KeyError(f"Ticket ID {ticket_id} not found. Please check available tickets.")
            if new_status.lower() not in ["open", "closed"]:
                raise ValueError("Status must be 'open' or 'closed'.")
            
            old_status = self.service_tickets[ticket_id]["Status"]
            self.service_tickets[ticket_id]["Status"] = new_status.lower()
            self.save_tickets()
            print(f"Ticket {ticket_id} status updated from '{old_status}' to '{new_status.lower()}'")
        except KeyError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_all_tickets(self, filter_status=None):
        try:
            if filter_status:
                filter_status = filter_status.lower()
                if filter_status not in ["open", "closed"]:
                    raise ValueError("Filter status must be 'open' or 'closed'.")
            
            tickets = {k: v for k, v in self.service_tickets.items() if v["Status"] == filter_status} if filter_status else self.service_tickets

            if tickets:
                for ticket_id, details in tickets.items():
                    print(f"{ticket_id}: Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")
            else:
                if filter_status:
                    print(f"No tickets found with status '{filter_status}'.")
                else:
                    print("No tickets found.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_ticket(self, ticket_id):
        try:
            if ticket_id not in self.service_tickets:
                raise KeyError(f"Ticket ID {ticket_id} not found. Please check available tickets.")
            return self.service_tickets[ticket_id]
        except KeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return None
