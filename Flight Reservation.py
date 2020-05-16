# A simple program to explain threading.
from threading import *
from time import sleep

class flightReservation:
    def __init__(self,ticket_left):
        self.ticket_left = ticket_left
    
    def buy(self,ticketRequest):
        if(self.ticket_left>=ticketRequest):
            print("Your tickets are confirmed")
            print("Make payment and collect tickets")
            self.ticket_left -= ticketRequest
        else:
            print("Sorry, not enough tickets remaining")

res = flightReservation(8)
t1 = Thread(target=res.buy,args=[3])
t2 = Thread(target=res.buy,args=[4])
t3 = Thread(target=res.buy,args=[3])
t1.start()
t2.start()
t3.start()