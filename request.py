class Requests:
    """The request class manages the submition of requests via
    the initializition. It keeps track of pending requests, status = open.

    The methods in this class deals with accepting a request, which 
    iniatiates the cancelition of requests that shared the time slot.

    The other major method deals with informing the users affect by acepting
    a request. The notify method sends an email if your req was accepted/declined"""

    def __init__(self, user_info,  date, time_slots):
        self.user_info = user_info
        self.date = date
        self.time_slots = time_slots

    def submit_req(self, schedule):
        schedule[self.date]['pending'].append(self)

    def get_req(self):
        print(self)
