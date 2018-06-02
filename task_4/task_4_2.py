class CinemaTickets(object):

    def __init__(self, film, hall, row, place, date, time, ticket_price):
        self.film = film
        self.hall = hall
        self.row = row
        self.place = place
        self.date = date
        self.time = time
        self.ticket_price = ticket_price

    def buy_ticket(self, film, hall, row, place, date, time, ticket_price):
        self.film = film,
        self.hall = hall,
        self.row = row,
        self.place = place,
        self.date = date,
        self.time = time,
        self.ticket_price = ticket_price

    def print_info(self):
        print("Film: ", self.film)
        print("Hall: ", self.hall)
        print("Row date: ", self.row)
        print("Place: ", self.place)
        print("Date: ", self.date)
        print("Time: ", self.time)
        print("Ticket price: ", self.ticket_price)


visitor1 = CinemaTickets('Interstellar', 'Big blue', 5, 12, '01.06.2018', '18.00', 7)
visitor2 = CinemaTickets('Paint It Black', 'Small red', 6, 13, '02.06.2018', '18.00', 5)
visitor3 = CinemaTickets('Paint It Black', 'Small red', 6, 14, '02.06.2018', '18.00', 5)
visitor1.print_info()
visitor2.print_info()
visitor3.print_info()
